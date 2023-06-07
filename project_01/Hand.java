/**
 * File: Card.java
 * Author: Harsha Somaya
 * CS231 Lab c/d
 * Monte-Carlo Simulation: Blackjack
 * wolfe/bender
 * Date: 02/08/2022
 * create a ahnd that will hold cards
 */
import java.util.ArrayList;

public class Hand {
    
    ArrayList<Card> myhand;
   
    public Hand (){
        myhand= new ArrayList<Card>();
    }
    
    public void reset(){
        myhand= new ArrayList<Card>();
    }   ///this recreates myhand to a new array list, so teh dynamic memory is involved since the old hand is replaced
   
    public void add(Card card){
        myhand.add(card);
    }
    
    public int size(){
;        return myhand.size();
    }
    
    public Card getCard(int i ){
        return myhand.get(i);
    }
   
    public int getTotalValue(){
        int value=0;
        
        for (int index=0;index<size(); index++){
                value+=getCard(index).getValue();}
       
                return value;
    }

    public String toString(){  
        String inital="";
        for (int index=0;index<size(); index++){
            inital+= "Card at index "+index+" has a "+getCard(index).toString();
        }    
            //return myhand.toString();
        
            return inital;
}

public static void main( String [] ar){  ///make to string separate
    Hand testing=new Hand();
    Card firstcard=new Card(17);
    testing.add(firstcard);
    System.out.println("first total value: "+ testing.getTotalValue());
    System.out.println("first to string: "+testing.toString());
    System.out.println("first size: "+testing.size());
    Card secondcard=new Card(20);
    testing.add(secondcard);
    System.out.println("seocnd total value: "+ testing.getTotalValue());
    System.out.println("second to string: "+testing.toString());
    System.out.println("second size: "+testing.size());
    Card thirdcard=new Card(10);
    testing.add(thirdcard);
    System.out.println("third size: "+testing.size());
    System.out.println("3rd total value: "+ testing.getTotalValue());
    System.out.println("3rd to string: "+testing.toString());

}
}
