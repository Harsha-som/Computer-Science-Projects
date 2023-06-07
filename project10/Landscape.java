/**
 * Harsha Somaya
 * 03/18/2022
 * Section Lab C/D
 * Project 6
 * CS 231
 * Landscape.java
 */

import java.awt.Graphics;
import java.util.ArrayList;
import java.awt.Font;
import java.awt.Color;


public class Landscape {
    /**
     * fields for landscape
     */
    public Hunter hunter;
    public Wumpus wumpus;
    private int width;
    private int height;
    public ArrayList<Vertex> vertexList;
    
    public Landscape(int w, int h, ArrayList<Vertex> listOfNodes ){
        /**
         * landscape constructor 
         */
        width=w;
        height=h;
        vertexList=listOfNodes;
        width=w;
        height=h;
        for (int i=0; i<5; i++){
            for (int j=0;j<5;j++){   //keeping x the same, but y is increasing cause j is increasing, adds it by row. gooing down a row
                vertexList.add(new Vertex(i, 5+j,true));
            }
        }

        for (int i=0;i<vertexList.size()-1;i++){  //connect before to after 
            vertexList.get(i).connect(vertexList.get(i+1)); // these two are the vertical  //connect down a row
            vertexList.get(i+1).connect(vertexList.get(i)); //connect up a row
            if (i < vertexList.size()-5){   
                vertexList.get(i).connect(vertexList.get(i+5)); //these two are the horizontal  //connects to the right 
                vertexList.get(i+5).connect(vertexList.get(i)); //connect to left
            }
        }
        hunter=new Hunter(vertexList.get(0));
        wumpus=new Wumpus (vertexList.get(1));
    }
        
    

    public Landscape(int w, int h ){
        /**
         * 2nd landscape constructor 
         */
        width=w;
        height=h;
        vertexList=new ArrayList<Vertex>();
    
        // for (int i=0; i<5; i++){
        //     for (int j=0;j<5;j++){
        //         vertexList.add(new Vertex(i, 5+j,true));
        //     }
        // }

        // for (int i=0;i<vertexList.size()-1;i++){  //connect before to after 
        //     vertexList.get(i).connect(vertexList.get(i+1)); // these two are the vertical
        //     vertexList.get(i+1).connect(vertexList.get(i));
        //     if (i < vertexList.size()-5){
        //         vertexList.get(i).connect(vertexList.get(i+5)); //these two are the horizontal
        //         vertexList.get(i+5).connect(vertexList.get(i));
        //     }
        // }
        // hunter=new Hunter(vertexList.get(0));
        // wumpus=new Wumpus (vertexList.get(1));

    }

    public int getHeight() {
        /**
         * return the height of the Landscape
         */
        return height;
    }

    public int getWidth() {
        /**
         * return the width of the Landscape.
         */
        return width;
    }

    public String toString(){
        /**
         * return a string indicating how many vertixces aare in the landscape.
         */
        return "there are "+ vertexList.size()+" vertici";
    }

    public void addBackgroundAgent(Vertex v){
        /**
         * add vertices to the landcape
         */
            vertexList.add(v);
        
    }

    public void moveUp(){
        /**
         * move hunter up
         */
        int x=hunter.currentVertex.getXPosition();
        int y=hunter.currentVertex.getYPosition();
        System.out.println(hunter.currentVertex);
        if (hunter.currentVertex.getNeighbor(x, y-1)!=null){
            hunter.currentVertex=hunter.currentVertex.getNeighbor(x, y-1);
        }
    }

    public void moveLeft(){
        /**
         * move hunter left
         */
        int x=hunter.currentVertex.getXPosition();
        int y=hunter.currentVertex.getYPosition();
        if (hunter.currentVertex.getNeighbor(x-1, y)!=null){
            hunter.currentVertex=hunter.currentVertex.getNeighbor(x-1, y);
        }
    }

    
    public void moveDown(){
        /**
         * move hunter down
         */
        int x=hunter.currentVertex.getXPosition();
        int y=hunter.currentVertex.getYPosition();
        if (hunter.currentVertex.getNeighbor(x, y+1)!=null){
            hunter.currentVertex=hunter.currentVertex.getNeighbor(x, y+1);
        }
    }

    public void moveRight(){
        /**
         * move hunter irght
         */
        int x=hunter.currentVertex.getXPosition();
        int y=hunter.currentVertex.getYPosition();
        if (hunter.currentVertex.getNeighbor(x+1, y)!=null){
            hunter.currentVertex=hunter.currentVertex.getNeighbor(x+1, y); }
    }




    public void attackRight(){
        /**
         * attack if pressed space and d
         */
        System.out.println("attacking right");
        int x=hunter.currentVertex.getXPosition();
        int y=hunter.currentVertex.getYPosition();
        if (hunter.currentVertex.getNeighbor(x+1, y)!=null){
            if (wumpus.homeVertex==hunter.currentVertex.getNeighbor(x+1, y)){
                wumpus.dead();
            }
            else{
                hunter.dead();
            }
        }
    }

    public void attackLeft(){
        /**
         * attack if pressed space and a
         */
        int x=hunter.currentVertex.getXPosition();
        int y=hunter.currentVertex.getYPosition();
        if (hunter.currentVertex.getNeighbor(x-1, y)!=null){
            System.out.println("line ");
            if (wumpus.homeVertex== hunter.currentVertex.getNeighbor(x-1, y)){
                wumpus.dead();
            }
            else{
                hunter.dead();
            }
        }
    }

    public void attackUp(){
        /**
         * attack if pressed space and w
         */
        int x=hunter.currentVertex.getXPosition();
        int y=hunter.currentVertex.getYPosition();
        if (hunter.currentVertex.getNeighbor(x, y-1)!=null){
            if (wumpus.homeVertex==hunter.currentVertex.getNeighbor(x, y-1)){
                wumpus.dead();
            }
            else{
                hunter.dead();
            }
        }
    }

    public void attackDown(){
        /**
         * attack if pressed space and s
         */
        System.out.println("attacking down");
        int x=hunter.currentVertex.getXPosition();
        int y=hunter.currentVertex.getYPosition();
        if (hunter.currentVertex.getNeighbor(x, y+1)!=null){
            if (wumpus.homeVertex==hunter.currentVertex.getNeighbor(x, y+1)){
                wumpus.dead();
            }
            else{
                hunter.dead();
            }
        }
    }



    public void draw(Graphics g, int scale){
        /**
         * loop through the CheckoutAgents, calling the draw method on each.
         */

        for (Vertex vertex:vertexList ) {  //for eery cashier
        vertex.draw(g,scale);  //draw the cashier
        }
        // wumpus.draw(g,scale); //draw wumpus only if deads COMMENT OUT
        hunter.draw(g, scale);
        if (hunter.alive==false || wumpus.alive==false || wumpus.victory){  //if it kills the hunter
            wumpus.draw(g,scale); //draw wumpus only if deads
            drawEndState(g);
        }
        
        
    }

    public void drawEndState(Graphics g){
        /**
         * draws end of the game state
         */
        if (hunter.alive){
            g.setColor(Color.GREEN);
            g.setFont(new Font("Arial", Font.PLAIN, 25));
            g.drawString("You won!", 80, 100);
        }
        else{
            g.setColor(Color.RED);
            g.setFont(new Font("Arial", Font.PLAIN, 25));
            g.drawString("You lost!", 80, 100);
        }     
    }



  
    

    
    public static void main(String[] args) {
        /**
         * main method for testing
         */
        Landscape scape=new Landscape(500, 500);
        Vertex v1 = new Vertex( 0, 0);
        v1.setVisibility( true );
        v1.setCost( 0 );
        Vertex v2 = new Vertex( 0, 1 );
        v2.setVisibility( true );
        v2.setCost( 1 );
        Vertex v3 = new Vertex( 0, 2 );
        v3.setVisibility( true );
        v3.setCost( 2 );
        Vertex v4 = new Vertex( 0, 3 );
        v4.setVisibility( true );
        v4.setCost( 3 );
        v1.connect( v2, Vertex.Direction.EAST );
        v2.connect( v1, Vertex.Direction.WEST );
        v2.connect( v3, Vertex.Direction.EAST );
        v3.connect( v2, Vertex.Direction.WEST );
        v3.connect( v4, Vertex.Direction.EAST );
        v4.connect( v3, Vertex.Direction.WEST );
        scape.addBackgroundAgent( v1 );
        scape.addBackgroundAgent( v2 );
        scape.addBackgroundAgent( v3 );
        scape.addBackgroundAgent( v4 );  
        System.out.println("height should be 500  "+scape.getHeight());   
        System.out.println("width should be 500 "+scape.getHeight());  
        System.out.println("to string is "+scape.toString());       
     
    
    }

}
