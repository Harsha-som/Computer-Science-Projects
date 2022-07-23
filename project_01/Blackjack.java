/**
 * File: Card.java
 * Author: Harsha Somaya
 * CS231 Lab c/d
 * Monte-Carlo Simulation: Blackjack
 * wolfe/bender
 * Date: 02/08/2022
 * create a single blackjack game 
 */
public class Blackjack {
   
    Deck deck = new Deck();
    Hand phand = new Hand();
    Hand dhand = new Hand();
    int cardbelow;

    public Blackjack(int reshuffleCutoff) {
        cardbelow = reshuffleCutoff;
        reset();

    }

    public void reset() {
        
        if (deck.size() < cardbelow) {
            Deck shuffleddeck = new Deck();
            shuffleddeck.shuffle();
            deck = shuffleddeck;
        } //at this point deck is set equal to shuffled deck, so dynamic meory is involved
        ///since after this point the old deck is lost
        
        else {
            phand.reset();
            dhand.reset();

        }
    }    

    public void deal() {
        phand.add(deck.deal());
        phand.add(deck.deal());
        dhand.add(deck.deal());
        dhand.add(deck.deal());
    }

    public boolean playerTurn() {
        
        int vlaueofp = phand.getTotalValue();
       
        while (vlaueofp < 17) {
            phand.add(deck.deal());
            vlaueofp = phand.getTotalValue();
        }
        
        if (vlaueofp > 21) {
            //System.out.println("playeeeer total value "+phand.getTotalValue()+"\n");
            return false;
        }
       
        // System.out.println("player total value "+phand.getTotalValue()+"\n");
        
       return true;
    }  



    public boolean dealerTurn() {
        
        int vlaueofd = dhand.getTotalValue();
        
        while (vlaueofd < 18) {
            dhand.add(deck.deal());
            vlaueofd = dhand.getTotalValue();
        }
       
        if (vlaueofd > 21) {
            //System.out.println("dealerrrr total value "+dhand.getTotalValue()+"\n");
            return false;
       
        }
       
        //System.out.println("dealer total value "+dhand.getTotalValue()+"\n");
        return true;
    }

    public void setReshuffleCutoff(int cutoff) {
        cardbelow = cutoff;
    }

    public int getReshuffleCutoff() {
        return cardbelow;
    }

    public String toString() {
        return "player hand: " + phand + "dealer hand: " + dhand + " player total vlaue is " + phand.getTotalValue()
        + " dealer total vaue is " + dhand.getTotalValue();
    }

    public int game (boolean verbose) {
        
        reset();
        deal();
        String initalp=phand.toString();
        String iniitald=dhand.toString();
        boolean playeroutput=playerTurn();
        int gamestate=-1;
        boolean playerwins=false;
        
        if (playeroutput==true){
            boolean dealeroutput=dealerTurn();
        
            if (dealeroutput==false){
                gamestate= 1;
                playerwins=true;
            }
         
            else if (dealeroutput==true){
               
                if (dhand.getTotalValue()>phand.getTotalValue()){
                    gamestate= -1;}
               
                    else if (dhand.getTotalValue()<phand.getTotalValue()){
                    playerwins=true;
                    gamestate= 1;}
               
                    else if (dhand.getTotalValue()==phand.getTotalValue()){
                    gamestate= 0;
                }
                
            }
        };

        if (verbose==true){
            System.out.println("Inital player hand (after dealing 2 cards): "+initalp+ "Inital dealer hand (after dealing 2 cards): "+iniitald);
            System.out.println("final player hand: "+phand.toString()+ " final dealer hand: "+ dhand.toString());
            System.out.println("the output is "+ gamestate+", which means the statement the player wins is "+playerwins);
        }
       
        return gamestate;
    }

    public static void main(String[] args) {
        System.out.println("\n 1st game: ");
        Blackjack firstgame = new Blackjack(30);
        firstgame.game(true);
        System.out.println("\n 2nd game: ");
        Blackjack secondgame = new Blackjack(30);
        secondgame.game(true);
        System.out.println("\n 3rd game: ");
        Blackjack thirdgame = new Blackjack(30);
        thirdgame.game(true);
        // // System.out.println(firstgame.toString()); //iitally empty
        // firstgame.deal(); /// give both 2
        // System.out.println(firstgame.toString());

        // System.out.println(firstgame.playerTurn()); // false if busts, true if not bust
        // // System.out.println(firstgame.toString());
        // System.out.println(firstgame.dealerTurn());
        // System.out.println(firstgame.toString());

    }
}
