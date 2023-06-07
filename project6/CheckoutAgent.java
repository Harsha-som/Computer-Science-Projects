/**
 * Harsha Somaya
 * 03/18/2022
 * Section Lab C/D
 * Project 6
 * CS 231
 * CHeckoutAgent.java
 */

import java.awt.Graphics;
import java.util.ArrayList;

public class CheckoutAgent {
    private int x;
    private int y;
    private MyQueue<Customer> queue;

    public CheckoutAgent(int x, int y){
        /**
         * constructor for checkout agent class
         */
        this.x=x;
        this.y=y;
        queue= new MyQueue<>();

    }

    public void addCustomerToQueue( Customer c ){
        /**
         * add a Customer to its queue
         */
        queue.offer(c);
    }

    public int getNumInQueue(){
        /**
         * returns the number of Customers in its queue.
         */
        return queue.size();
    }

    public void draw(Graphics g){
        /**
         *  draws the CheckoutAgent as a rectangle near the bottom of the window with a height proportional to the number of Customers in the queue. 
         */
        //arguments represent upper left after subtraction 
        g.drawRect(x, y-(70*queue.size()), 50, 70*queue.size());  //for every customer in size, go up 70 pixels
        int customerIndex=0;
        for (Customer customer: queue){
            customerIndex++;
            customer.draw(g,x, y-70*customerIndex);
        }
    }

    public void updateState(Landscape scape){
        /**
         * update teh state of each customer in the queue 
         */
        for (Customer customer:queue ){
            customer.incrementTime();
        }
        if (!queue.empty()){
            Customer current=queue.peek();
            current.giveUpItem();   
            if (current.getNumItems()==0) {  //after they giave up have nothing
                queue.poll();
                scape.addFinishedCustomer(current);
            } 
        }      
    }

    public static void main(String[] args) {
        /**
         * main method to test the checkout agents
         */
        CheckoutAgent testAgent= new CheckoutAgent(250, 370);
        System.out.println("there should be 0 customers: "+testAgent.getNumInQueue());
        RandomCustomer testCustomer= new RandomCustomer(5);
        testAgent.addCustomerToQueue(testCustomer);
        System.out.println("there should now be 1 customer: "+testAgent.getNumInQueue());
        ArrayList<CheckoutAgent> testArray= new ArrayList<>(5);
        Landscape testLandscape= new Landscape(500, 250, testArray);
        testAgent.updateState(testLandscape);

    }

}
