/**
 * Harsha Somaya
 * 03/18/2022
 * Section Lab C/D
 * Project 6
 * CS 231
 * Pick2CustomerSimulation.java
 */

import java.util.Random;
import java.util.ArrayList;
public class Pick2CustomerSimulation {
    public static void main(String[] args) throws InterruptedException {
        /**
         *main method for testing picky2 customer
         */
        Random gen = new Random();
        ArrayList<CheckoutAgent> checkouts = new ArrayList<CheckoutAgent>(5);

        for(int i=0;i<5;i++) {
            CheckoutAgent checkout = new CheckoutAgent( i*100+50, 480 );
            checkouts.add( checkout );
        }
        Landscape scape = new Landscape(500,500, checkouts);
        LandscapeDisplay display = new LandscapeDisplay(scape);
        
        for (int j = 0; j < 999; j++) {
            Customer cust = new Pick2Customer(1+gen.nextInt(7));  //between 0 and 9  +1==1 and 10 items
            int choice = cust.chooseLine( checkouts );
            checkouts.get(choice).addCustomerToQueue( cust );  //checkouts.get(choice) returns line choosen out of the list
            scape.updateCheckouts();
            display.repaint();
            Thread.sleep( 250 );
            if (j%100==0 && j!=0){
                scape.printFinishedCustomerStatistics();
            }
        }

    }
}