/**
 * Harsha Somaya
 * 04/05/2022
 * Section Lab C/D
 * Project 9
 * CS 231
 * KVTestComparatorTwo.java
 */
import java.util.Comparator;

public class KVTestComparatorTwo implements Comparator<KeyValuePair<String,Integer>> {
        public int compare( KeyValuePair<String,Integer> i1, KeyValuePair<String,Integer> i2 ) {
            /**
             * compare based on key's value
             */
            // returns negative number if i2 comes after i1 lexicographically
            float diff = i1.getValue() - i2.getValue();
            if (diff == 0.0)
                return 0;
            if (diff < 0.0)  //if i2 is bigger than i1, give a negative  
                return -1;
            else
                return 1;  //if i1 is igge rthan i1, gie positive number  
        }
    }
    

