/**
 * Harsha Somaya
 * 03/18/2022
 * Section Lab C/D
 * Project 6
 * CS 231
 * PickyCustomer.java
 */
import java.util.ArrayList;

public class PickyCustomer extends Customer{
    public PickyCustomer( int num_items, int num_lines ){
        /**
         * calls the parent class customer constructor 
         */
        super(num_items, num_lines);
    }


    public int chooseLine(ArrayList<CheckoutAgent> checkouts) {
        /**
         * returns the index of the CheckoutAgent with the shortest line.
         */
        int inital=500;
        int index=0;
        for (int i=0; i<checkouts.size(); i++){
            if (checkouts.get(i).getNumInQueue()<inital){  //if one checkout cashier has less customers then the next one
                index=i;
                inital=checkouts.get(i).getNumInQueue();
            }
        }
        return index;

        }
    
}
