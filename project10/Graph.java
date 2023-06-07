/**
 * Harsha Somaya
 * 04/05/2022
 * Section Lab C/D
 * Project 10
 * CS 231
 * Graph.java
 */


import java.util.ArrayList;
import java.util.PriorityQueue;


public class Graph {
    private ArrayList<Vertex> list;  

    public Graph(){
        /**
         * cosntructor
         */
        list=new ArrayList<>();

    }

    public int vertexCount(){
        /**
         *  returns the number of vertices in the graph
         */
        return list.size();
    }

    public boolean inGraph(Vertex query){
        /**
         * return true if the query Vertex is in the graph's vertex list.
         */
        if (list.contains(query)){
            return true;
        }
        return false;
    }


    public ArrayList<Vertex> getVertices(){
        /**
         * returns an array list of all of teh graph vertices
         */
       return list;
    }


    public void addUniEdge(Vertex v1, Vertex v2){
        /**
         * adds v1 and v2 to the graph (if necessary) and adds an edge connecting v1 to v2, creating a uni-directional link.
         */
        if (!list.contains(v1) && !list.contains(v2)){  //if both do not exist 
            list.add(v1);
            list.add(v2);
            v1.connect(v2);
        }

        else {  //if one exists  
            boolean conatinsv1=list.contains(v1) ;
            boolean conatinsv2=list.contains(v2) ;
            if (!conatinsv2){
                list.add(v2);
            }

            else if (!conatinsv1){
                list.add(v1);
            }
            v1.connect(v2);
        }
    }

    public void addBiEdge(Vertex v1, Vertex v2){
        /**
         * adds v1 and v2 to the graph (if necessary), adds an edge connecting v1 to v2, and adds a second edge connecting v2 to v1, creating a bi-directional link.
         */
        if (!list.contains(v1) && !list.contains(v2)){  //if both do not exist 
            list.add(v1);
            list.add(v2);
            v1.connect(v2);
            v2.connect(v1);
        }

        else {  //if one exists  
            boolean conatinsv1=list.contains(v1) ;
            boolean conatinsv2=list.contains(v2) ;
            if (!conatinsv2){
                list.add(v2);
            }

            else if (!conatinsv1){
                list.add(v1);
            }
            v1.connect(v2);
            v2.connect(v1);
        }
    }

    public void shortestPath(Vertex v0){
        /**
         * implements a single-source shortest-path algorithm for the Graph, Dijkstra's algorithm.
         */
        for (Vertex indiviudalVertex: list){
            indiviudalVertex.setVisited(false);
            indiviudalVertex.setCost( 1e+7);
            indiviudalVertex.setParent(null);
        }
        PriorityQueue<Vertex> queue=new PriorityQueue<Vertex>();  
        v0.setCost(0.0);
        queue.add(v0);
        while (!queue.isEmpty()){ //while this que is not empty 
            Vertex v=queue.remove();//whatever i added last //give vertetx with lowest distance 
            if (v.getVisited()){
                continue;  //back to line  104
            }
            v.setVisited(true);
            for (Vertex w: v.getNeighbors()){
                double distance= v.distance(w);
                if (!w.getVisited() && v.getCost()+distance<w.getCost()){
                    w.setCost(v.getCost()+distance);
                    w.setParent(v);
                    queue.add(w);
                }
            }
        }
    }

        public static void main(String[] args) {
            /**
             * main method for testing
             */
            Graph test=new Graph();
            Vertex vertex1= new Vertex(0, 2, false);
            Vertex vertex2= new Vertex(7, 9, false);
            Vertex vertex3= new Vertex(14, 12, false);
            Vertex vertex4= new Vertex(2, 5, false);
            Vertex vertex5= new Vertex(13, 7, false);
            Vertex vertex6= new Vertex(8, 18, false);
            Vertex vertex7= new Vertex(10, 11, false);
            Vertex vertex8= new Vertex(15, 12, false);
            Vertex vertex9= new Vertex(5, 7, false);
            Vertex vertex10= new Vertex(11, 13, false);  

            test.addBiEdge(vertex1, vertex2);
            test.addBiEdge(vertex4, vertex6);
            test.addUniEdge(vertex2, vertex3);
            test.addUniEdge(vertex2, vertex5);
            test.addUniEdge(vertex2, vertex6);
            test.addUniEdge(vertex1, vertex7);
            test.addBiEdge(vertex4, vertex8);
            test.addBiEdge(vertex6, vertex8);
            test.addUniEdge(vertex3, vertex9);
            test.addUniEdge(vertex3, vertex10);

            System.out.println("should be 6 "+test.vertexCount());
            System.out.println("should be true  "+test.inGraph(vertex6));
            System.out.println("before "+test.list);  
            test.shortestPath(vertex2);
            System.out.println("after "+test.list);

        }
    }



