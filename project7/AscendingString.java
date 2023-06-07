/**
 * Harsha Somaya
 * 04/05/2022
 * Section Lab C/D
 * Project 7
 * CS 231
 * AscendingString.java
 */

import java.util.Comparator;

public class AscendingString implements Comparator<String>{

    public int compare(String arg, String arg2){
        /**
         * abstract method for comparing two string arguments 
         */
        return arg.compareTo(arg2);
    }

  
}


