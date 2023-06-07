/**
 * Harsha Somaya
 * 03/18/2022
 * Section Lab C/D
 * Project 5
 * CS 231
 */
import java.awt.Graphics;

public class Agent {
    private double x;
    private double y;

    public Agent(double x0, double y0) {
        /**
         * a constructor that sets the position.
         */
        x = x0;
        y = y0;
    }

    public double getX() {
        /**
         * returns the x position.
         */
        return x;
    }

    public double getY() {
        /** returns the y position. */
        return y;
    }

    public void setX(double newX){
        /**
         * sets teh x position
         */
        x=newX;
    }

    public void setY(double newY){
        /**
         * sets teh y position
         */
        y=newY;
    }

    public String toString(){
        /**
         * returns a String containing the x and y positions
         */
        return "x is "+String.valueOf(x)+" y is "+ String.valueOf(y);
    }

    public void updateState( Landscape scape ) {
        /**
         * 
         */
    }

    public void draw (Graphics g){

    }

    public static void main(String[] args) {
        /**
         * test the agent class
         */
        Agent myAgent= new Agent(4.7,8.9);
        System.out.println(myAgent.getX());
        System.out.println(myAgent.getY());
        myAgent.setX(3.4);
        myAgent.setY(2);
        System.out.println( myAgent.toString());        

    }


}
