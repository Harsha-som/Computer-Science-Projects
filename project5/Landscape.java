/**
 * Harsha Somaya
 * 03/18/2022
 * Section Lab C/D
 * Project 5
 * CS 231
 */
import java.util.ArrayList;
import java.awt.Graphics;

public class Landscape {
    /**
     * fields to store its width and height (as ints) and a LinkedList of Agents
     */
    private int width;
    private int height;
    private LinkedList<Agent> agentList;

    public Landscape(int w, int h) {
        /**
         * a constructor that sets the width and height fields, and initializes the
         * agent list.
         */
        width = w;
        height = h;
        agentList = new LinkedList<Agent>();
    }

    public int getHeight() {
        /**
         * returns the height.
         */
        return height;
    }

    public int getWidth() {
        /**
         * returns the width
         */
        return width;
    }

    public void addAgent(Agent A) {
        /**
         * inserts an agent at the beginning of its list of agents.
         */
        agentList.addFirst(A);
    }

    public String toSTring() {
        /**
         * returns a String representing the Landscape. It can be as simple as
         * indicating the number of Agents on the Landscape.
         */
        return agentList.toArrayList().toString();
        // return String.valueOf(agentList.size());
    }

    public ArrayList<Agent> getNeighbors(double x0, double y0, double radius) {
        /**
         * returns a list of the Agents within radius distance of the location x0, y0.
         */
        ArrayList<Agent> arrayList = new ArrayList<>();
        for (Agent agent : agentList) {
            // if (agent.getX() <= x0 + radius && agent.getX() >= x0 - radius && agent.getY() <= y0 + radius
            //         && agent.getY() >= y0 - radius) {
            //     arrayList.add(agent);
            // }
            // double xDistance= Math.pow((agent.getX()-x0),2);
            // double yDistance=Math.pow((agent.getY()-y0),2);
            // if (Math.sqrt(xDistance+yDistance)<=radius && agent.getX()!=x0 && agent.getY()!=y0  ){
            //     arrayList.add(agent);
            // }
            if (Math.hypot(agent.getX()-x0, agent.getY()-y0)<=radius    ){
                 arrayList.add(agent);

            }
        }
        return arrayList;
    }

    public void draw(Graphics g) {
        /**
         * Calls the draw method of all the agents on the Landscape.
         */
        for (Agent agent : agentList) {
            agent.draw(g);
        }
    }

    public void updateAgents(){
        /**
         * update the state of each agent, in a random order
         */
        ArrayList<Agent> list= agentList.toShuffledList();
        for (Agent agent:list){
            agent.updateState(this);
        }
    }


    public static void main(String[] args) {
        /**
         * tests the class
         */
        // my test
        Landscape myLandscape= new Landscape(63, 100);
        // System.out.println(myLandscape.getHeight());
        // System.out.println(myLandscape.getWidth());
        // System.out.println(myLandscape.toSTring());
        // myLandscape.addAgent(new Agent(4, 11)); //y out of range
        // myLandscape.addAgent(new Agent(6, 9));
        // myLandscape.addAgent(new Agent(7, 9)); //x out of range
        // myLandscape.addAgent(new Agent(5, 8));
        // myLandscape.addAgent(new Agent(4, 7));
        // System.out.println(myLandscape.toSTring());
        // System.out.println("new");
        // System.out.println(myLandscape.getNeighbors(4, 7, 2)); //might need to make astring of teh arraylist, not call method in here
        SocialAgent test=new SocialAgent (5,5,10);
        myLandscape.addAgent(test);
        myLandscape.addAgent(new SocialAgent (10,10,10));
        myLandscape.addAgent(new SocialAgent (15,15,10));
        myLandscape.addAgent(new SocialAgent (20,20,10));
        System.out.println(myLandscape.getNeighbors(test.getX(),test.getY(),15));
        test.updateState(myLandscape);
        System.out.println(test);





    }

}
