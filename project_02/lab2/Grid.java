/**
 * Cell.java
 * Represents a 2d array/grid
 * Harsha Somaya
 * CS231 S22
 * Project 2
 */
import java.util.Random;

public class Grid {
    /**
     * create a grid of inetegrs
     */
    public static void main(String [] args) {
        if (args.length<1){
            System.out.println("please provide an array so the program can print every element in the String array.");
        }
        for (String element:args )  {
            System.out.println(element); }
        int yogi=Integer.parseInt(args[0]);
        int booboo=Integer.parseInt(args[1]);
        // System.out.println(yogi);
        // System.out.println(booboo);
        String[][] ranger= new String [yogi][booboo];  //array of nulls
        // String[][] rangger;   //null--less memeory for declaration
        // rangger=new String [yogi][booboo];  //array of nulls
        //System.out.println(ranger);
        Random random=new Random();
        for (int row=0; row<yogi; row++){
            for (int column=0; column<booboo; column++){
                int value=random.nextInt(26)+97;
                ranger[row][column]="" + (char)value;
            }
        }
            for (int row=0; row<ranger.length; row++){
                for (int column=0; column<ranger[row].length; column++){
                    System.out.print(ranger[row][column]+" | ");
                }
            System.out.println();
            System.out.println("---------------------------");
        }  
        
    } 
} 
