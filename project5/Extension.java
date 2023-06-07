/**
 * Harsha Somaya
 * 03/18/2022
 * Section Lab C/D
 * Project 5
 * CS 231
 */
import java.util.Scanner;

public class Extension {
    /**
     * evaluates the extension
     * @param args
     * @throws InterruptedException
     */
    public static void main(String[] args) throws InterruptedException{
        /**
         * runs the extension
         */
        Scanner scan = new Scanner(System.in); // Create a Scanner object
        System.out.println("Which simulation do you want to run? Social Agent or Cat Social Agent");
        String input = scan.nextLine();
        if (input.equals("Social Agent")) {
            System.out.println("You selected social agent. What is your timestep, landscape width, height, radius, and agent number ");
            int[] newArray= new int[5];
            for (int i=0;i<5;i++){
                int arguments = scan.nextInt();
                newArray[i]=arguments;
            }
            SocialAgentSimulationExtension simulationOptionOne = new SocialAgentSimulationExtension(newArray);
            scan.close();
        } else if (input.equals("Cat Social Agent")) {
            System.out.println("You selected catsocial agent. What is your timestep, landscape width, height, radius, agent number, and number of categories ");
            int[] newArray= new int[6];
            for (int i=0;i<6;i++){
                int arguments = scan.nextInt();
                newArray[i]=arguments;
            }
            CatSocialAgentSimulationExtension simulationOptionTwo = new CatSocialAgentSimulationExtension(newArray);
            scan.close();
        }
        else{
            System.out.println("oops u have incorrect answer; rerun again");
        }

    }
}
