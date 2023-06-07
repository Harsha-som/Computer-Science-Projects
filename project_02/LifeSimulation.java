/**
 * LifeSimulation.java
 * Represents a Connoway's game an x number of times updating  
 * Harsha Somaya
 * CS231 S22
 * Project 2
 */
import java.util.Random;
public class LifeSimulation { 
    /**
     * contain all the code for the class that will 
     * run the game
     */
    public static void main(String[] args) throws InterruptedException {
        /**
         * have the main that wil test and actually create the simulation
         */
        Landscape scape = new Landscape(Integer.parseInt(args[1]),Integer.parseInt(args[2]));
        Random gen = new Random();
        double density = Float.parseFloat(args[3]);
     
        // initialize the grid to be 30% full
        for (int i = 0; i < scape.getRows(); i++) {
            for (int j = 0; j < scape.getCols(); j++ ) { 
                scape.getCell( i, j ).setAlive( gen.nextDouble() <= density );
            }
        }

        LandscapeDisplay display = new LandscapeDisplay(scape, 8);
        int timestep=0;
        while (timestep<Integer.parseInt(args[0])){
            scape.advance();
            Thread.sleep( 250 );
            display.repaint();
            timestep++;
        }
    }
}       

