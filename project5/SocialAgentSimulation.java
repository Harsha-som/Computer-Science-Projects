/**
 * Harsha Somaya
 * 03/18/2022
 * Section Lab C/D
 * Project 5
 * CS 231
 */
import java.util.Random;

public class SocialAgentSimulation {
    public static void main(String[] args) throws InterruptedException {
        /**
         * have the main that wil test and actually create the simulation
         */
        Landscape scape = new Landscape(Integer.parseInt(args[1]), Integer.parseInt(args[2]));
        LandscapeDisplay display = new LandscapeDisplay(scape);
        Random random= new Random();

        for (int i = 0; i < 200; i++) {  //2*upperlimit=(0,upper*2)-lower=(lower, 2upper-lower)
           SocialAgent newAgent= new SocialAgent(random.nextDouble() *Integer.parseInt(args[1]),random.nextDouble() *Integer.parseInt(args[2]),15);
           scape.addAgent(newAgent);
        }
    

        int timestep=0;
        while(timestep<Integer.parseInt(args[0])){
            scape.updateAgents();
            display.repaint();
            Thread.sleep(250);
            timestep++;
        }
    }
}
