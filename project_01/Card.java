/**
 * File: Card.java
 * Author: Harsha Somaya
 * CS231 Lab c/d
 * Monte-Carlo Simulation: Blackjack
 * wolfe/bender
 * Date: 02/08/2022
 * create new randomized Arraylists
 */
import java.util.Random;

public class Card {
    
    private int cardvalue;

    public Card(int value){
    if (value<2 ) {  //how to range check
        System.out.println("Inputed card value is out of range");
    }
    cardvalue=value;
}

public int getValue(){
    return cardvalue ;

}

public String toString(){   //usually returns memnory location then, how to call, leave empty?
    return "card value of "+cardvalue+ "\n";

}
public static void main (String [] agx){
    Random random=new Random();
    int value=random.nextInt(10)+2;  //random number from 2 to 11 inclusive
    Card newCard=new Card(value);     //create new card from 2 to 12
    System.out.println(newCard); 
    System.out.println("the value is again with getValue: "+newCard.getValue());

}
}
