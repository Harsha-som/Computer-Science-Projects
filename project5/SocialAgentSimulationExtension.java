/**
 * Harsha Somaya
 * 03/18/2022
 * Section Lab C/D
 * Project 5
 * CS 231
 */
import java.util.Random;


public class SocialAgentSimulationExtension {
        /**
         * have the main that wil test and actually create the simulation
         */
        public SocialAgentSimulationExtension(int[] args) throws InterruptedException{

        
        Landscape scape = new Landscape(args[1], args[2]);
        LandscapeDisplay display = new LandscapeDisplay(scape);
        Random random= new Random();

        for (int i = 0; i < args[4]; i++) {  //2*upperlimit=(0,upper*2)-lower=(lower, 2upper-lower)
           SocialAgent newAgent= new SocialAgent(random.nextDouble() *args[1],random.nextDouble() *args[2],args[3]);  //fix string to radius
           scape.addAgent(newAgent);
        }
    

        int timestep=0;
        while(timestep<args[0]){
            scape.updateAgents();
            display.repaint();
            Thread.sleep(250);
            timestep++;
        }
    }
    }

