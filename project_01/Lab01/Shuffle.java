/**
 * File: Shuffle.java
 * Author: Harsha Somaya
 * Date: 02/08/2022
 * create new randomized Arraylists
 */
import java.util.ArrayList;
import java.util.Random;
public class Shuffle {
    public static void main ( String[] args )	{ 
        ArrayList<Integer> mylist=new ArrayList<Integer>();
        System.out.println(mylist);
        for (int i=0; i<10; i++){
            Random random=new Random();
            int value=random.nextInt(100); 
            mylist.add(value);  //add value between 1 and 99 inclusive
            System.out.println(mylist.get(i));  }
           // System.out.println(mylist);
        for (int i=0; i<10; i++){
            Random random=new Random();
            int index=random.nextInt(mylist.size()); 
            System.out.print(mylist.get(index));
            mylist.remove(index);
            System.out.print( " is removed, arraylist is now "+  mylist);
                System.out.println(" ");
        }
        for (int i=0; i<10; i++){
            Random random=new Random();
            int value=random.nextInt(10)+1; //[1,10]
            mylist.add(value);
            //System.out.println( "testing" + mylist.get(i));  
            System.out.println("list is now" +mylist);
        }  
    ArrayList<Integer> newrandomlist=new ArrayList<Integer>();
    for (int i=0; i<10; i++){
        Random random=new Random();
        int index=random.nextInt(mylist.size());  ///give a random index from the 0 index up to the size but not including
        newrandomlist.add(mylist.get(index));  //get a value from my list at a rnadom index, add that to new random list
        //System.out.println( "testing" + mylist.get(i));  
        System.out.println("randomized list is now" +newrandomlist);
    }  
 
}
} 
