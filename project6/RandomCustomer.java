/**
 * Harsha Somaya
 * 03/18/2022
 * Section Lab C/D
 * Project 6
 * CS 231
 * RandomCustomer.java
 */
import java.util.Random;
import java.util.ArrayList;
public class RandomCustomer extends Customer{

    public RandomCustomer( int num_itemss ){
        /**
         * cosntructor calls customer constructor with given num_items and timesetp=1
         */
        super(num_itemss,1);
    }

    public int chooseLine(ArrayList<CheckoutAgent> checkouts){
        /**
         * returns an integer randomly chosen from the range 0 (inclusive) to the lenght of the list (exclusive).
         */
        Random randomGenerator= new Random();
        return randomGenerator.nextInt(checkouts.size()) ;
    }
    
}
