/**
 * Harsha Somaya
 * 04/05/2022
 * Section Lab C/D
 * Project 10
 * CS 231
 * Wumpus.java
 */

import java.awt.Graphics;
import java.util.ArrayList;
import java.util.Random;
import java.awt.Image;
import java.awt.Toolkit;


public class Wumpus {
    public Vertex homeVertex;
    public boolean alive;
    public boolean victory;

    // ArrayList<Vertex> allVertixes;

    public Wumpus(Vertex home){
        homeVertex=home;  
        // allVertixes=allVertices;
        alive=true;
        victory=false;
    }

    public void draw(Graphics g, int scale){
        /**
         * draw the Wumpus 
         */
        // ArrayList<Vertex> neighbors= homeVertex.getNeighbors();
        Image wumpusPic = Toolkit.getDefaultToolkit().getImage("wumpus.png");
        int xPos = homeVertex.getXPosition()*scale;
        int yPos=homeVertex.getYPosition()*scale;
        int border = 8;
        // g.drawRect(xPos + border, yPos + border, scale - 4*border, scale - 3 * border);
        g.drawImage(wumpusPic, xPos+border, yPos+border,scale - 4*border,scale - 3 * border, null  );
        
    }



    public void dead(){
        /**
         * dead pose activate 
         */
        alive=false;
        System.out.println("you won, wumpus killed!");
    }

    public void wumpusMoves(){
        /**
         * have teh wumpus move
         */
        ArrayList<Vertex> neighbors=homeVertex.getNeighbors();
        Random r=new Random();
        homeVertex=neighbors.get(r.nextInt(neighbors.size())); ///set the home vertex of the wumpus to be a random adjacent neighbor 
    }
    
}
