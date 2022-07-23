/**
 * Harsha Somaya
 * 04/05/2022
 * Section Lab C/D
 * Project 10
 * CS 231
 * Vertex.java
 */

import java.util.ArrayList;
import java.awt.Graphics;
import java.awt.Color;


public class Vertex implements Comparable<Vertex>{
    private ArrayList<Vertex> arrayList;
    private int x;
    private int y;
    private boolean vertexVisible;
    private double distance;
    private boolean nodeVisited;
    private Vertex parent;


    public Vertex(int x, int y, boolean visibility){
        /**
         * constructor for a vertex
         */
        this.x=x;
        this.y=y;
        vertexVisible=visibility;
        arrayList= new ArrayList<>();
        distance=0;
        nodeVisited=false;
        parent=null;
    }


    public Vertex(int x, int y){
        /**
         * 2nd constructor for a vertex
         */
        this.x=x;
        this.y=y;
        arrayList= new ArrayList<>();
        distance=0;
        nodeVisited=false;
        parent=null;
    }

    public Vertex(int x, int y, Direction uselessDirection){
        /**
         * 3nd constructor for a vertex
         */
        this.x=x;
        this.y=y;
        arrayList= new ArrayList<>();
        distance=0;
        nodeVisited=false;
        parent=null;
    }


    public int getXPosition(){
        /**
         * returns the x  location of vertex
         */
        return x;
    }


    public int getYPosition(){
        /**
         * returns the y location of vertex
         */
        return y;
    }


    public void setPosition(int newX,int newY){
        /**
         * set the x,y position to given argument s
         */
        x=newX;
        y=newY;
    }


    public boolean getVisibility(){
        /**
         * returns if the vertex is visible
         */
        return vertexVisible;
    }


    public void setVisibility(boolean visibile){
        /**
         * setxs the vertex visibility 
         */
        vertexVisible=visibile;
    }


    public double getDistance(){
        /**
         * returns distance from root node
         */
        return distance;
    }


    public void setDistance(double newDistance){
        /**
         * sets  distance from root node
         */
        distance=newDistance;
    }


    public boolean getVisited(){
        /**
         * returns if a node is visited 
         */
        return nodeVisited;
    }

    public void setVisited(boolean visited){
        /**
         * sets  if a node is visited 
         */
        nodeVisited=visited;
    }

    public Vertex getParent(){
        /**
         * returns the parent node 
         */
        return parent;
    }


    public void setParent(Vertex parent){
        /**
         * sets this node's parent 
         */
        this.parent=parent;
    }


    public double distance( Vertex other ){
        /**
         *  returns the Euclidean distance between this vertex and the other vertex based on their x and y positions.
         */
        double underSquareRoot=Math.pow((x-other.getXPosition()),2)+Math.pow((y-other.getYPosition()),2);    
        return Math.sqrt(underSquareRoot);
    }


    public void connect(Vertex other){
        /**
         * updates this vertex' adjacency list/map so that it connects with the other Vertex. This is a uni-directional link.
         */
        arrayList.add(other);
    }

    public void connect(Vertex other, Direction useless){
        /**
         * updates this vertex' adjacency list/map so that it connects with the other Vertex. This is a uni-directional link.
         */
        arrayList.add(other);
    }


    public Vertex getNeighbor(int x, int y){
        /**
         *  returns the Vertex at position (x, y) if the Vertex is in the adjacency list, otherwise null.
         */
        for (Vertex neighbor:arrayList){
            if (neighbor.getXPosition()==x && neighbor.getYPosition()==y){
                return neighbor;
            }
        }
        return null;
    }


    public ArrayList<Vertex> getNeighbors(){
        /**
         *  returns an ArrayList of type Vertex which contains all of this Vertex' neighbors.
         */
        return arrayList;
    }


    public int numNeighbors(){
        /**
         *  returns the number of connected vertices.
         */
        return arrayList.size();
    }


    public String toString(){
        /**
         * returns a String containing (at least) the number of neighbors, this Vertex' cost, and the marked flag.
         */
        return "the number of neighbors is "+numNeighbors()+" and the cost is "+distance +" visitation state is " +getVisited()+" for the vertext at "+getXPosition()+ ","+ getYPosition()+"\n";
    }


    public double getCost(){
        /**
         * returns the cost
         */
        return distance;
    }


    public void setCost(double cost){
        /**
         * sets the cost to the given double 
         */
        this.distance=cost;
    }


    public int compareTo(Vertex other){
        /**
         * rteurns a negative. positive, or 0 based on this vertex and the other's relationship
         */

        if (distance>((Vertex)other).getDistance()){
             return 1; 
        }

        else if (distance<((Vertex)other).getDistance()){
            return -1;
        }

        else{return 0;}


    }

    public static boolean matchPosition( Vertex a, Vertex b ){
        /**
         * returns true if the x and y positions of the two vertices match.
         */
        if (a.getXPosition()==b.getXPosition() && b.getYPosition()==a.getYPosition()){
            return true;
        }
        return false;
    }

    public enum Direction { EAST,WEST,NORTH,SOUTH };


    public void draw (Graphics g, int scale){
        /**
         * draws a vertex
         */
        if (!getVisibility()){
            return;
        }

        int xPos = (int)getXPosition()*scale;
        int yPos = (int)getYPosition()*scale;  
        int border = 2;
        int half = scale / 2;
        int eighth = scale / 8;
        int sixteenth = scale / 16;
        // draw rectangle for the walls of the room
        if (getCost() <= 2)  {// wumpus is nearby
            g.setColor(Color.red);
        }        

        else{  // wumpus is not nearby
            g.setColor(Color.pink);

        } 
        g.drawRect(xPos + border, yPos + border, scale - 2*border, scale - 2 * border);
        
        // draw doorways as boxes
        g.setColor(Color.black);
        if (getNeighbor( getXPosition(), getYPosition()-1 ) != null )
            g.fillRect(xPos + half - sixteenth, yPos, eighth, eighth + sixteenth);
        if (getNeighbor( getXPosition(), getYPosition()+1 ) != null )
            g.fillRect(xPos + half - sixteenth, yPos + scale - (eighth + sixteenth), 
                       eighth, eighth + sixteenth);
        if (getNeighbor( getXPosition()-1, getYPosition() )!=null)
            g.fillRect(xPos, yPos + half - sixteenth, eighth + sixteenth, eighth);
        if (getNeighbor( getXPosition()+1, getYPosition() )!=null)
            g.fillRect(xPos + scale - (eighth + sixteenth), yPos + half - sixteenth, 
                       eighth + sixteenth, eighth);
    }
				

    


    public static void main(String[] args) {
        /**
         * main method for testing 
         */
        Vertex test=new Vertex(4, 8, true);
        System.out.println("x is four "+ String.valueOf(test.getXPosition()==4));  //should be true
        System.out.println(" y is 8 "+test.getYPosition());
        System.out.println("should be true "+test.getVisibility());
        test.setPosition(9, 11);
        test.setVisibility(false);
        System.out.println("x is 9 "+ String.valueOf(test.getXPosition()==4));  //should be false
        System.out.println(" y is 11 "+test.getYPosition());
        System.out.println("should be false "+test.getVisibility());
        System.out.println(test.getDistance());
        test.setDistance(4.15);
        System.out.println("should be 4.15 "+ test.getDistance());
        System.out.println("false "+test.getVisited());
        test.setVisited(true);
        System.out.println("true "+test.getVisited());
        System.out.println("should be 0 "+test.distance);
        Vertex neighbor=new Vertex(7, 17, true);
        System.out.println("should be 0: "+test.numNeighbors());
        test.connect(neighbor);
        System.out.println("shoudl be null "+ test.getNeighbor(7,9));
        System.out.println("shoudl be true, so neighbor to string "+ test.getNeighbor(7,17));
        System.out.println("should be false "+matchPosition(test, neighbor));
        System.out.println("distance  "+test.distance(neighbor));
        System.out.println("should be 1 now: "+test.numNeighbors());
        System.out.println("should now have 1 neighbor "+test.getNeighbors());
        test.setDistance(14.8);
        System.out.println("should be 14.8 "+test.getDistance());
        System.out.println("should be 1 "+test.compareTo(neighbor));
        test.setParent(neighbor);
        System.out.println("should have the parent toString()"+test.getParent());
        test.setCost(4.75);
        System.out.println("should be 4.75 "+test.getCost());

    }

 }