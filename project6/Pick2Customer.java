
/**
 * Harsha Somaya
 * 03/18/2022
 * Section Lab C/D
 * Project 6
 * CS 231
 * Pick2Customer.java
 */
import java.util.Random;
import java.util.ArrayList;;

public class Pick2Customer extends Customer {
    /** 
     * @param num_items
     */
    public Pick2Customer(int num_items) {
        /**
         * call the parent customer constructor with num_items and time step 2
         */
        super(num_items, 2);
    }

    public int chooseLine(ArrayList<CheckoutAgent> checkouts) {
         /**
         * returns the index of the shorter of two randomly chosen queues
         */
        Random r = new Random();
        int firstLineIndex= r.nextInt(checkouts.size());
        int secondLineIndex= r.nextInt(checkouts.size());
        while (secondLineIndex==firstLineIndex){
            secondLineIndex= r.nextInt(checkouts.size());
        }
        if (checkouts.get(firstLineIndex).getNumInQueue()<checkouts.get(secondLineIndex).getNumInQueue()){  //if one checkout cashier is shorter then the next one
           return firstLineIndex;
        }
        else{
            return secondLineIndex;
        }
    }
}
