/**
 * Landscape.java
 * Represents Conway game of life, creating a landcape
 * Harsha Somaya
 * CS231 S22
 * Project 2
 */
import java.util.ArrayList;

import javax.print.event.PrintJobListener;

import java.awt.Graphics;

public class Landscape{
    /**
     * visulaizes the landscpae where the cells will be
     */
    Cell[][] mylandscape;
    int rows;
    int columns;
    public Landscape(int rows, int cols){
        this.rows=rows;
        this.columns=cols;
        mylandscape=new Cell[rows][columns];
        //Then it should allocate a Cell for each location in the Grid.
        for (int r=0; r<rows;r++){
            for (int c=0;c<columns; c++){
                mylandscape[r][c]=new Cell();  //the new Cell can only be found for this scope of code
            }
        }
    }

    public void reset(){
        /**
         * call teh rest method on every cell
         */
        for (int r=0; r<rows;r++){
            for (int c=0;c<columns; c++){
                mylandscape[r][c].reset();
            }
        }
    }

    public int getRows(){ 
        /**
         * return # of rows in landscape
         */
        return rows;
    }

    public int getCols(){
        /**
         * return # of columns in landscape
         */
        return columns;
    }

    public Cell getCell( int row, int col ) {
        /**
         * retrun cell at specifiedd row and column
         */
        return mylandscape[row][col];
    }

    public String toString(){
        String mystring="";
        /**
         * calls the to string method for eveyr cell, visualizing the landscape
         */
        for (int r=0; r<rows;r++){
            for (int c=0;c<columns; c++){
                mystring+=mylandscape[r][c];  //cell adding to string, hmm computer thinks let me add cell's to string
            }
        mystring+="\n";
        }        
        return mystring;
    }

    public ArrayList<Cell> getNeighbors( int row, int col ){  ///assume row and col are the indexes
        /**
         * return neighbors of specifiecd cell
         */
        ArrayList<Cell> refrences= new ArrayList<Cell>();  //this new array list of cells is accessible for this scope of code
        if (col<(mylandscape[row].length)-1){ ///meaning something to the right
            refrences.add(mylandscape[row][col+1]); //return elemnet to right
        }
        if (col >0 && col<mylandscape[row].length){  //meaning something to teh left since not 1st column
            refrences.add(mylandscape[row][col-1]); 

        }
        if (row < mylandscape.length-1 ){  //return cell below
            refrences.add(mylandscape[row+1][col]);

        }
        if (row <mylandscape.length && row>0){  //return cell above
            refrences.add(mylandscape[row-1][col]);

        }
        refrences.add(mylandscape[0][0]);  //return top left
        refrences.add(mylandscape[0][(mylandscape[0].length)-1]); //return top right
        refrences.add(mylandscape[(mylandscape.length)-1][0]); //return bottom left
        int bottomRowIndex=(mylandscape.length)-1;
        refrences.add(mylandscape[bottomRowIndex][(mylandscape[bottomRowIndex].length)-1]);  //return bottom right
        return refrences;   //scope of code ends
    }

    public void draw( Graphics g, int gridScale ){
        /**
         * call call draw method of every cell
         */
        for (int i=0; i<mylandscape.length; i++){//row
            for (int j=0;j<mylandscape[i].length-1;j++){ 
                mylandscape[i][j].draw(g,j*gridScale, i*gridScale, gridScale);
            }
        }   
    }

    public void advance(){
        /**
         * advance the landscape based on teh surrounding neighbors
         */
        Cell[][] temporary= new Cell[rows][columns];
        System.out.println("temporary before:");
        System.out.println(temporary.toString());
        for (int r=0; r<rows;r++){
            for (int c=0;c<columns; c++){
                temporary[r][c]=new Cell(mylandscape[r][c].isAlive);  //nessary, copies string aove but not status
            }
        }
        for (int r=0; r<rows;r++){
            for (int c=0;c<columns; c++){
                temporary[r][c].updateState(getNeighbors(r, c));  //how does computer know it is the r and c of mylandscape/orginal grid
            }
        }
        mylandscape=temporary;
        // System.out.println("after");
        // System.out.println(mylandscape.toString());

    }

    public static void main(String[] args){
        /**
         * test all of the landscape methods by cretaing a object
         */
        Landscape firstlLandscape= new Landscape(4, 3);
        System.out.println(firstlLandscape);
        // System.out.println(firstlLandscape.getNeighbors(0, 1));
        // System.out.println("should be 4"+ firstlLandscape.getRows());
        // System.out.println("should be 3"+ firstlLandscape.getCols());
        // System.out.println("shoudl be -1"+firstlLandscape.getCell(0,1));
        // ArrayList<Cell> neighbors=firstlLandscape.getNeighbors(2, 1);
        //Cell mycell= firstlLandscape.mylandscape[2][1];
        Cell cell1=firstlLandscape.mylandscape[3][1];
        cell1.setAlive(true);
        Cell cell2=firstlLandscape.mylandscape[2][2];
        cell2.setAlive(true);
        // System.out.println("before");
        // System.out.println(firstlLandscape);
        // System.out.println("after");
        Cell cell3=firstlLandscape.mylandscape[2][0];
        cell3.setAlive(true);
        // mycell.updateState(neighbors);
        // System.out.println(firstlLandscape);
        // System.out.println(neighbors);
        System.out.println(firstlLandscape);
        firstlLandscape.advance();
        System.out.println(firstlLandscape);
        firstlLandscape.advance();
        System.out.println("again");
        Cell cell4=firstlLandscape.mylandscape[3][2];
        cell4.setAlive(true);
        System.out.println(firstlLandscape);
        firstlLandscape.advance();

    }

}