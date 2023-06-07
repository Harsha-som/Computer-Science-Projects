
/**
 * File: Card.java
 * Author: Harsha Somaya
 * CS231 Lab c/d
 * Monte-Carlo Simulation: Blackjack
 * wolfe/bender
 * Date: 02/08/2022
 * simulate multiple blackjack games
 */
import java.util.ArrayList;
public class Simulation {
//     public static void main(String[] args) {
//         int playerwincount=0;
//         int dealerwincount=0;
//         int pushcount=0;
//         Blackjack blackjackobject= new Blackjack(31);
//         for (int i=0;i<1000; i++){
//             int gamestate=blackjackobject.game(false);
//             if (gamestate==-1){
//                 dealerwincount+=1;}
//             else if (gamestate==1){
//                 playerwincount+=1;}
//             else if (gamestate==0){
//                 pushcount+=1;}
//             }
//             //System.out.println("The player won "+playerwincount+ " games, while the dealer won "+ dealerwincount+" games. There were " + pushcount + " pushes. 
//             //This means that the player % is" +playerwincount/1000+" the dealer % is "+dealerwincount/1000+" and the push % is "+ pushcount/1000);
//             System.out.println("The player won "+ playerwincount+" times, while the dealer won "+ dealerwincount+" times. \nThe player average % wins is "+ ((float)playerwincount/10)+
//             ", while the dealer avaerage % win is "+((float)dealerwincount/10)+". \nNumber of pushes is "+pushcount+", meaning the pushes average is "+((float)pushcount/10));
//         }
    

    public static void main(String[] args) {
        int playerwincount=0;
        int dealerwincount=0;
        int pushcount=0;
        Blackjack blackjackobject= new Blackjack(31);
        ArrayList<Integer> playerlist=new ArrayList<Integer>();
        ArrayList<Double> meanminussquare=new ArrayList<Double>();
        ArrayList<Double> listofstdev= new ArrayList<Double>();
        listofstdev = new ArrayList<Double>();;

       for (int j=0; j<16; j++){
        int gamestate=blackjackobject.game(false);

            for (int i=0;i<4; i++){
             
                if (gamestate==-1){
                    dealerwincount+=1;}
               
                    else if (gamestate==1){
                    playerwincount+=1;}
               
                    else if (gamestate==0){
                    pushcount+=1;}
                    playerlist.add(playerwincount);
                    System.out.println("The player won "+ playerwincount+" times, while the dealer won "+ dealerwincount+" times. \nThe player average % wins is "+ ((float)playerwincount/10)+
                    ", while the dealer avaerage % win is "+((float)dealerwincount/10)+". \nNumber of pushes is "+pushcount+", meaning the pushes average is "+((float)pushcount/10)); 
                }
        }
       
        System.out.println(playerlist);
        
        double mean=0;
        
        double numerator=0;

        for (int i=0;i<playerlist.size();i++){
            mean+=playerlist.get(i);
        }
        
        for (int i=0;i<playerlist.size();i++){
            Double squared = Math.pow((playerlist.get(i)-mean), 2);
            meanminussquare.add(squared) ;
        }
       
        for (int i=0;i<meanminussquare.size();i++){
            numerator+=meanminussquare.get(i);
        }
double undersquareroot=numerator/playerlist.size();

double standardeviation=Math.sqrt(undersquareroot);

listofstdev.add(standardeviation);

System.out.println("The standard deviation for the player wins is "+standardeviation);
}
}
    
    
