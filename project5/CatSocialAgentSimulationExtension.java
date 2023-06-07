/**
 * Harsha Somaya
 * 03/18/2022
 * Section Lab C/D
 * Project 5
 * CS 231
 */
import java.util.Random;

public class CatSocialAgentSimulationExtension {
    public CatSocialAgentSimulationExtension(int[] args) throws InterruptedException {
        /**
         * call the respective ocnstructor so that teh extension can be displayed
         */
        Landscape scape = new Landscape(args[1], args[2]);
        LandscapeDisplay display = new LandscapeDisplay(scape);
        Random random = new Random();

        for (int i = 0; i < (args[4]); i++) { // 2*upperlimit=(0,upper*2)-lower=(lower, 2upper-lower)
            CatSocialAgent newAgent = new CatSocialAgent(random.nextDouble() * (args[1]),random.nextDouble() * (args[2]), random.nextInt(args[5]), (args[3]));
            scape.addAgent(newAgent);
        }

        int timestep = 0;
        while (timestep < (args[0])) {
            scape.updateAgents();
            display.repaint();
            Thread.sleep(250);
            timestep++;
        }
    }
}
