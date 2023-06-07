/**
 * File: Card.java
 * Author: Harsha Somaya
 * CS231 Lab c/d
 * Monte-Carlo Simulation: Blackjack
 * wolfe/bender
 * Date: 02/08/2022
 * create a deck with 52 cards
 */
import java.util.ArrayList;
import java.util.Random;

public class Deck {
ArrayList <Card> mydeck;

public Deck(){
       build(); 
       shuffle();
}

public void build (){
    mydeck=new ArrayList <Card> ();

    for (int outsershape=0;outsershape<4;outsershape++){//adds 8 cards 4 times
        
        for (int i=2; i<10; i++){ ///makes card from 2 to 9, adds 8 cards
            mydeck.add(new Card(i)); //dynamic memory for new card being added lost after this point
        }  
    }

    for (int i=0; i<16; i++){  ///adds 16 10 cards
        mydeck.add(new Card(10)); //dynamic memory for card w/ face value 10 being added lost after this point
    }

    for (int i=0; i<4; i++){ ///adds 4 11 cards
        mydeck.add(new Card(11));  //dynamic memory for card w/ face value 11 being added lost after this point
    }

}

public int size(){
    return mydeck.size();
}

public Card deal(){
   Card topcard=mydeck.get(0);
    mydeck.remove(0);
    return topcard;
}

public Card pick(int i){
    Card picked=mydeck.get(i);
     mydeck.remove(i);
     return picked;
 }

 public void shuffle(){   ///can get the generator to a call a random number multiples times, but because remove it the card at 13 is not the same card
    ///everytime because you are removing
    
    int size=mydeck.size();
    
    ArrayList <Card> shuffled= new  ArrayList<Card>();  
    
    for (int i=0;i<size;i++){
        Random random=new Random();
        int randomindex=random.nextInt(size-i);    //mydeck.size   i- how many cards taken out   //max 52-0=52=[51] inclusive index (last card in my deck)
        //i goes to 51, 52-51=1, [0] inclusive, nly card in my deck after u removed everything
        shuffled.add(mydeck.remove(randomindex));  //returns card and adds to shuffled
    }  //random object lost after this point
   
    mydeck=shuffled;
 }   ///shuffled dynamic memory lost after this point

 public String toString(){
    return mydeck.toString();
    }

public static void  main(String[] agx){
    Deck firstdeck=new Deck();
    System.out.println(firstdeck.size());
    System.out.println(firstdeck);  ///Card toString() automatic why printed
    System.out.println("deal "+firstdeck.deal()); 
    System.out.println("pick "+firstdeck.pick(46));
    firstdeck.shuffle();
    System.out.println(firstdeck.toString());


}
}
