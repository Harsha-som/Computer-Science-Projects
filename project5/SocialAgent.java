/**
 * Harsha Somaya
 * 03/18/2022
 * Section Lab C/D
 * Project 5
 * CS 231
 */
import java.awt.Graphics;
import java.awt.Color;
import java.util.Random;
import java.util.*;

public class SocialAgent extends Agent {
    private boolean moved;
    public int radius;

    public SocialAgent(double x0, double y0, int radius) {
        /**
         * The constructor, which calls the super class constructor and sets the radius
         * field.
         */
        super(x0, y0);
        this.radius = radius;
    }

    public SocialAgent(double x0, double y0) {
        /**
         * The constructor, which calls the super class constructor and sets the radius
         * field.
         */
        super(x0, y0);
        radius = 5;
    }
    public void setRadius(int radius) {
        /**
         * sets the cell's radius of sensitivity to the value of radius
         */
        this.radius = radius;
    }

    public int getRadius() {
        /**
         * rteurn cell raidus of sensitivity
         */
        return radius;
    }

    public void draw(Graphics g) {
        /**
         * draws a circle of radius 5 (i.e. it fits in a 10x10 box) at the Agent's
         * location.
         */
        if (moved) {
            g.setColor(Color.lightGray);
            g.drawOval((int) getX(), (int) getY(), 5, 5);

        } else {
            g.setColor(Color.darkGray);
            g.drawOval((int) getX(), (int) getY(), 5, 5);
        }
    }

    public void updateState(Landscape scape) {
        /**
         * updates the cell states based on rules
         */
        ArrayList<Agent> a = scape.getNeighbors(getX(), getY(), radius);
        Random random= new Random();
        a.remove(this);
        if (a.size()>3  ){  //if in clumop
            if (random.nextFloat()<.01){  //if number between 0 and 1 is less than .01 //1%chance 
                setX((getX()+random.nextFloat()*20-10)); // [0,1)*20=[0,20)-10=[-10,10)
                setY(getY()+random.nextFloat()*20-10); // [0,1)*20=[0,20)-10=[-10,10) 
                moved=true;
            }
            else{  //99% of time and in clump do not movee
                moved=false;
            }
        }
        else{  //not in clump, move
            setX(getX()+random.nextFloat()*20-10); // [0,1)*20=[0,20)-10=[-10,10)
            setY(getY()+random.nextFloat()*20-10); // [0,1)*20=[0,20)-10=[-10,10) 
            moved=true;
        }
    }

    public boolean getMoved(){
        /*
        returns is moved
         */
        return moved;
    }

    public void setMoved(boolean move){
        /**
         * sets the moved field
         */
        moved=move;
    }

    
    public static void main(String[] args) {
        /**
         * main method to test class
         */
        SocialAgent myAgent = new SocialAgent(4.7, 8.9, 2);
        System.out.println(myAgent.getX());
        System.out.println(myAgent.getY());
        myAgent.setX(3.4);
        myAgent.setY(2);
        System.out.println(myAgent.toString());
        myAgent.setRadius(4);
       System.out.println(myAgent.getRadius());
       
    }

}
