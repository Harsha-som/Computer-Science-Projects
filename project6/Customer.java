/**
 * Harsha Somaya
 * 03/18/2022
 * Section Lab C/D
 * Project 6
 * CS 231
 * Customer.java
 */

import java.util.ArrayList;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.Toolkit;
import java.awt.Color;



public abstract class Customer {
    /**
     * fields for customer
     */
    private int timeStep;
    private int remaningItems;


    public Customer(int num_items){
        /**
         * first constructor 
         */
        timeStep=0;
        remaningItems=num_items;
    }


    public Customer(int num_items, int time_steps){
        /**
         * second costructor with two items
         */
        timeStep=time_steps;
        remaningItems=num_items;
    }


    public void incrementTime(){
        /**
         * increments the number of time steps.
         */
        timeStep++;
    }


    public int getTime(){
        /**
         *  returns the number of time steps
         */
        return timeStep;
    }

    public void draw(Graphics g, int x, int y){
        /**
         * draw the customers onto landscape
         */
        Image customerPic = Toolkit.getDefaultToolkit().getImage("customer.jpg");
        g.drawImage(customerPic, x, y,50,50, Color.pink, null  );
        g.drawString(""+remaningItems, x, y-3);
    }

    public void giveUpItem(){
        /**
         * decrements the number of items (indicating another item has been paid for).
         */
        remaningItems--;
    }

    public int getNumItems(){
        /**
         *  returns the number of items.
         */
        return remaningItems;
    }

    public abstract int chooseLine(ArrayList<CheckoutAgent> checkouts);
    
}
