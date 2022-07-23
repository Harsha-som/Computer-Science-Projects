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

public class Landscape {
    /**
     * fields for landscape
     */
    private int width;
    private int height;
    private ArrayList<CheckoutAgent> agentsList;
    private LinkedList<Customer> completedCustomers;
    
    public Landscape(int w, int h, ArrayList<CheckoutAgent> checkouts ){
        /**
         * landscape constructor 
         */
        completedCustomers= new LinkedList<>();
        width=w;
        height=h;
        agentsList=checkouts;
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
         * return a string indicating how many checkouts and finished customers are in the landscape.
         */
        return "there are "+ agentsList.size()+" lines availiable for checkout and "+completedCustomers.size()+" completed customers";
    }

    public void addFinishedCustomer(Customer c ){
        /**
         * add the Customer to the list of finished customers.
         */
        completedCustomers.addFirst(c);
    }

    public void draw(Graphics g){
        /**
         * loop through the CheckoutAgents, calling the draw method on each.
         */
        for (CheckoutAgent checkOutAgent:agentsList ) {  //for eery cashier
           checkOutAgent.draw(g);  //draw the cashier
          
        }
    }

    public void updateCheckouts(){
        /**
         * update state for every checkout agent in the list
         */
        for (CheckoutAgent line:agentsList){
            line.updateState(this);
        }
    }

    public void printFinishedCustomerStatistics(){
        /**
         *  compute and print the average and standard deviation of the time-to-leave for all of the Customers in the finished customer list.
         */
        float time=0;
        double standardDeviation=0;
        for (Customer completed:completedCustomers){
            time+=completed.getTime();
        }
        float average=time/completedCustomers.size();
        System.out.println("the average is "+average);
        for (Customer completed:completedCustomers){
            standardDeviation+=Math.pow((completed.getTime()-average),2);
        }
        standardDeviation=Math.sqrt(standardDeviation/completedCustomers.size());
        System.out.println("the standard deviation is "+standardDeviation);
    }
    
    public static void main(String[] args) {
        /**
         * main method for testing
         */
        ArrayList<CheckoutAgent> checkouts=new ArrayList<>(25);
        Landscape myLandscape=new Landscape(500, 250, checkouts);
        System.out.println(myLandscape.getHeight()==250);  //true
        System.out.println(myLandscape.getWidth()==550);  //fale
        System.out.println(myLandscape.getWidth()==500);  //true
        System.out.println(myLandscape.toString());  //size should be 0, completed customrs should be 0
    }

}
