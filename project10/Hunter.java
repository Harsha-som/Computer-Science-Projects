/**
 * Harsha Somaya
 * 03/18/2022
 * Section Lab C/D
 * Project 6
 * CS 231
 * Hunter.java
 */

import java.awt.Graphics;
import java.awt.Image;
import java.awt.Toolkit;


 public class Hunter{
    public Vertex currentVertex;
    public boolean aim;
    public boolean alive;
    

    public Hunter(Vertex startVertex){
        /**
         * constructor for hunter
         */
        currentVertex=startVertex;
        aim=false;
        alive=true;
    }



    public void draw(Graphics g, int scale){
        /**
         * draw the hunter as an image
         */
        int xPos = currentVertex.getXPosition()*scale;
        Image hunterPic = Toolkit.getDefaultToolkit().getImage("hunter.png");

        int yPos=currentVertex.getYPosition()*scale;
        int border = 2;
        // g.drawRect(xPos + border, yPos + border, scale - 4*border, scale - 3 * border);
        g.drawImage(hunterPic, xPos+border, yPos+border,scale - 4*border,scale - 3 * border, null  );


    }

    public void dead(){
        /**
         * set the state for hunter if died
         */
        alive=false;
        System.out.println("end of game, you lost");
    }

 

 }
