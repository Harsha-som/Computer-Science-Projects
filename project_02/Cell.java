/**
 * Cell.java
 * Represents a single cell 
 * Harsha Somaya
 * CS231 S22
 * Project 2
 */

import java.awt.Color;
import java.awt.Graphics;
import java.util.ArrayList;

public class Cell {
   /**
    * creates a single cell, with teh default being dead
    */
   boolean isAlive;

   public Cell() {
      /**
       * cell is defualt to dead
       */
      isAlive = false;
   }

   public Cell(boolean alive) {
      /**
       * make cell's state equal to given parameter
       */
      isAlive = alive;
   }

   public boolean getAlive() {
      /**
       * return cell's state
       */
      return isAlive;
   }

   public void reset() {
      /**
       * kill teh cell
       */
      isAlive = false;
   }

   public void setAlive(boolean alive) {
      /**
       * make cell state be equal to argument
       */
      isAlive = alive;
   }

   public String toString() {
      /**
       * to string method that represents cell death as 0/-1
       */
      if (isAlive) {
         return "0 ";
      } else {
         return "-1 ";
      }
   }

   public void draw(Graphics g, int x, int y, int scale) {
      /**
       * draw the cell as ovals and have them colored
       */
      g.drawOval(x, y,  scale, scale);
      if (isAlive) {
         g.setColor(Color.DARK_GRAY);
         g.fillOval(x, y, scale,  scale);
      }
      else{
         g.setColor(Color.PINK);
         g.fillOval(x, y, scale, scale);
      }
   }

   public void updateState(ArrayList<Cell> neighbors) {
      /**
       * update the cell state depending on the neighbor's
       */
      int aliveNeighbors = 0;
      for (Cell cell : neighbors) {
         if (cell.isAlive) {
            aliveNeighbors += 1;
         }
      }
      if (!isAlive && aliveNeighbors == 3){
         setAlive(true);
      }
      else if (isAlive && (aliveNeighbors == 2 || aliveNeighbors == 3))  {
         setAlive(true);
      }
      else{
         setAlive(false);
      }

   }

   public static void main(String[] args) {
      /**
       * main method for testing the cell and its corersponding state
       */
      Cell mycell = new Cell(true);
      System.out.println(mycell.isAlive);
      System.out.println(mycell.getAlive());
      System.out.println("this shoudl be 0 " + mycell.toString());
      mycell.setAlive(false);
      System.out.println(mycell.isAlive);
      System.out.println(mycell.getAlive());
      System.out.println("this shoudl be -1 " + mycell);
      mycell.setAlive(true);
      System.out.println(mycell.isAlive);

   }

}
