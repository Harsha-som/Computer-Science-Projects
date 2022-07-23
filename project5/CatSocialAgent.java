/**
 * Harsha Somaya
 * 03/18/2022
 * Section Lab C/D
 * Project 5
 * CS 231
 */
import java.awt.Graphics;
import java.util.Random;
import java.util.ArrayList;
import java.awt.Color;


public class CatSocialAgent extends SocialAgent {
    private int category;
    private Color color;
    private int radius;

    public CatSocialAgent(double x0, double y0, int cat) {
        /**
         * calls the parent constructor and set the category.
         */
        super(x0, y0);
        category = cat;
        Random r= new Random(category);
        int colorOne=r.nextInt(256);
        int colorTwo=r.nextInt(256);
        int colorThree=r.nextInt(256);
        color= new Color(colorOne,colorTwo,colorThree);
    }

    public CatSocialAgent(double x0, double y0, int cat, int radius) {
        /**
         * calls the parent constructor and set the category.
         */
        super(x0, y0);
        category = cat;
        Random r= new Random(category);
        int colorOne=r.nextInt(256);
        int colorTwo=r.nextInt(256);
        int colorThree=r.nextInt(256);
        color= new Color(colorOne,colorTwo,colorThree);
        this.radius=radius;
    }

    public int getCategory() {
        /**
         * returns category
         */
        return category;
    }

    public String toString() {
        /**
         * returns a single character string indicating the category.
         */
        return ""+category;
    }

    public void draw(Graphics g) {
        /**
         * draws a circle of radius 5 (i.e. it fits in a 10x10 box) at the Agent's
         * location
         */

        if (getMoved()) {
            g.setColor(color.brighter());
            g.drawOval((int) getX(), (int) getY(), 5, 5);

        } else {
            g.setColor(color);
            g.drawOval((int) getX(), (int) getY(), 5, 5);
        }
    }

    public void updateState(Landscape scape){
        /**
         * updates state based on rules
         */
        Random random= new Random();
        ArrayList<Agent> a = scape.getNeighbors(getX(), getY(), radius);
        int cat= getCategory();
        int sameCategory=0;
        for (Agent agent: a){
            if (agent instanceof CatSocialAgent  && ((CatSocialAgent)agent).getCategory()==cat){
                sameCategory++;
            }
        }

        if (a.size()>=2 && sameCategory>=a.size()/2){
            if (random.nextFloat()<.01){  //if number between 0 and 1 is less than .01  
                setX((getX()+random.nextFloat()*20-10)); // [0,1)*20=[0,20)-10=[-10,10)
                setY(getY()+random.nextFloat()*20-10); // [0,1)*20=[0,20)-10=[-10,10) 
                setMoved(true);
            }
            else{
                setMoved(false);
            }
        }
        else{  //not in clump, move
            setX(getX()+random.nextFloat()*20-10); // [0,1)*20=[0,20)-10=[-10,10)
            setY(getY()+random.nextFloat()*20-10); // [0,1)*20=[0,20)-10=[-10,10) 
            setMoved(true);
        }
    }
}


