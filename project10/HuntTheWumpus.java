/**
 * Template created by Bruce A. Maxwell and Stephanie R Taylor
 * Harsha Somaya
 * 04/05/2022
 * Section Lab C/D
 * Project 10
 * CS 231
 * HuntTheWumpus.java
 */

import java.awt.BorderLayout;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.awt.Graphics;
import java.awt.Dimension;
import java.awt.Color;
import java.awt.event.MouseEvent;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JFrame;
import javax.swing.event.MouseInputAdapter;
import java.util.ArrayList;


public class HuntTheWumpus {
    private int spacePressed;
    private Graph graph;
    private Hunter hunter;
    private Wumpus wumpus;
    private ArrayList<Vertex> vertexList;
    private Landscape scape;
    private int scale;
    private JFrame win;
    private LandscapePanel canvas;    
    private JLabel fieldX; // Label field 1, displays the X location of the mouse 
    private JLabel fieldY;
    private JLabel aim;
    public enum PlayState { PLAY, STOP }
    public PlayState state;


    public HuntTheWumpus() {
        /**
         * sets all the fields of the game
         */
        spacePressed=0;
        state=PlayState.PLAY;
        win = new JFrame("Hunt the Wumpus");
        win.setDefaultCloseOperation( JFrame.EXIT_ON_CLOSE);
        scape=new Landscape(scale*10, scale*7);
        canvas = new LandscapePanel(scape.getWidth(),scape.getHeight() );
        win.add(canvas, BorderLayout.CENTER );
        win.pack();
        fieldX = new JLabel("X");
        fieldY = new JLabel("Y");
        JButton quit = new JButton("Quit");
        aim = new JLabel(" ");
        JPanel panel = new JPanel( new FlowLayout(FlowLayout.RIGHT));
        panel.add(aim);
        panel.add(fieldX );
        panel.add( fieldY );
        panel.add( quit );
        win.add( panel, BorderLayout.SOUTH);
        win.pack();
        Control control = new Control();
        this.win.addKeyListener(control);
        this.win.setFocusable(true);
        this.win.requestFocus();
        quit.addActionListener( control );
        MouseControl mc = new MouseControl();
        this.canvas.addMouseListener( mc );
        this.canvas.addMouseMotionListener( mc );

        // The last thing to do is make it all visible.
        this.win.setVisible( true );



        graph = new Graph();
        scale=64;
        vertexList = new ArrayList<>();
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) { // x is changing, y is constant
                vertexList.add(new Vertex(j + 5, i, true));
            }
        }
        scape.vertexList=vertexList;
        hunter=new Hunter(vertexList.get(0));
        wumpus=new Wumpus(vertexList.get(1));
        scape.hunter=hunter;
        scape.wumpus=wumpus;
        for (int i=0;i<vertexList.size()-1;i++){  //is last of one row not supposed to be connected to first of other
            if (i%5!=4){
                graph.addBiEdge(vertexList.get(i),vertexList.get(i+1));

            }
            if (i<vertexList.size()-5){  ///9 is max in exmaple 
                graph.addBiEdge(vertexList.get(i), vertexList.get(i+5));
            }
            
        }

    }

    private class LandscapePanel extends JPanel {
		
        public LandscapePanel(int height, int width) {
             /**
         * Creates the drawing canvas
         * @param height the height of the panel in pixels
         * @param width the width of the panel in pixels
         **/
            super();
            this.setPreferredSize( new Dimension( width, height ) );
            this.setBackground(Color.white);
        }

       
        public void paintComponent(Graphics g) {
             /**
         * Method overridden from JComponent that is responsible for
         * drawing components on the screen.  The supplied Graphics
         * object is used to draw.
         * 
         * @param g		the Graphics object used for drawing
         */
            super.paintComponent(g);
            scape.draw( g, scale );
        }
    } // end class LandscapePanel

    private class MouseControl extends MouseInputAdapter {
        public void mouseMoved(MouseEvent e) {
            /**
             * display the mouse location in x and y
             */
            fieldX.setText( "" + e.getPoint().x );
            fieldY.setText( "" + e.getPoint().y );
        }

        public void mouseDragged(MouseEvent e) {
            /**
             * display the mouse x and y if it is dragged
             */
            fieldX.setText( "" + e.getPoint().x );
            fieldY.setText( "" + e.getPoint().y );
        }
        
        public void mousePressed(MouseEvent e) {
            /**
             * print the # times the mouse was clicked at a certain spot
             */
            System.out.println( "Pressed: " + e.getClickCount() );
        }

        public void mouseReleased(MouseEvent e) {
             /**
             * print the # times the mouse was releassed at a certain spot, same number as the number of times a mouse is pressed
             */
            System.out.println( "Released: " + e.getClickCount());
        }

        public void mouseEntered(MouseEvent e) {
            /**
             * print the point hwere the mouse enters the window 
             */
            System.out.println( "Entered: " + e.getPoint() );
        }

        public void mouseExited(MouseEvent e) {
                /**
             * print the point hwere the mouse exists the window 
             */
            System.out.println( "Exited: " + e.getPoint() );
        }


    } // end class MouseControl

    private class Control extends KeyAdapter implements ActionListener {

        public void keyTyped(KeyEvent e) {
            /**
             * control all the game  rueles based on key pressed 
             */
            System.out.println( "Key Pressed: " + e.getKeyChar() );
            scape.wumpus.wumpusMoves();
            if( ("" + e.getKeyChar()).equalsIgnoreCase("q") ) {
                state = PlayState.STOP;
            }

            if( ("" + e.getKeyChar()).equalsIgnoreCase("w") ){
                if (scape.hunter.aim){
                    scape.attackUp(); 
                }
                else{scape.moveUp();}            
            }

            if( ("" + e.getKeyChar()).equalsIgnoreCase("a") ){
                if (scape.hunter.aim){
                    scape.attackLeft(); 
                }
                else{scape.moveLeft();}
            }

            if( ("" + e.getKeyChar()).equalsIgnoreCase("s") ){
                if (scape.hunter.aim){
                    scape.attackDown(); 
                }
                else{scape.moveDown();}
            }

            if( ("" + e.getKeyChar()).equalsIgnoreCase("d") ){
                if (scape.hunter.aim){
                    scape.attackRight(); 
                }
                else{scape.moveRight();}
            }

            if( ("" + e.getKeyChar()).equalsIgnoreCase(" ") ){
                spacePressed++;
                if (spacePressed%2==0){ //pressed two times
                    scape.hunter.aim=false;
                    aim.setText("not aiming");
                }
                else{System.out.println("here2");
                scape.hunter.aim=true;
                aim.setText("Aiming");
            }
            }
            repaint();


            if (scape.hunter.currentVertex==scape.wumpus.homeVertex){
                scape.hunter.alive=false;
                scape.wumpus.victory=true;
            }

            if (scape.hunter.alive==false || scape.wumpus.alive==false){
                state=PlayState.STOP;
            }
        }

        public void actionPerformed(ActionEvent event) {
            // If the Quit button was pressed, close the game 
            if( event.getActionCommand().equalsIgnoreCase("Quit") ) {
		        System.out.println("Quit button clicked");
                state = PlayState.STOP;
            }
        }

    } // end class Control

    public void repaint() {
        /**
         * redraws the  window 
         */
    	win.repaint();
    }

    public void dispose() {
        /**
         * close the window 
         */
	    win.dispose();
    }

    public static void main(String[] argv) throws InterruptedException {
        /**
         * main method that runs while game is on play mode 
         */
        HuntTheWumpus w = new HuntTheWumpus();
        while (w.state == PlayState.PLAY) {
            w.repaint();
            Thread.sleep(33);
        }
        Thread.sleep(2500);
        System.out.println("Disposing window");
        w.dispose();
    }

}