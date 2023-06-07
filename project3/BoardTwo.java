
/**
 * BoardTwo.java
*  Create the baord and be able to read txt files
 * Harsha Somaya
 * CS231 S22
 * Project 3/4
 * 3/7/2022
 * Lab C/D
 */
import java.io.*;
import java.awt.Graphics;
import java.awt.Color;
import java.awt.BasicStroke;
import java.awt.Graphics2D;
import java.awt.Font;

public class BoardTwo {
    /**
     * create a 2d arraw for a board
     */
    private Cell[][] cellArray;
    public static final int size = 9;

    public BoardTwo() {
        /**
         * Defines the Board fields and constructor
         */
        cellArray = new Cell[size][size];
        for (int r = 0; r < cellArray.length; r++) { 
            for (int c = 0; c < cellArray[r].length; c++) {
                cellArray[r][c] = new Cell();
            }
        }
    }

    public String toString() {
        /**
         * represent board as string
         */
        String theString = "";
        for (int r = 0; r < cellArray.length; r++) {
            for (int c = 0; c < cellArray[r].length; c++) {
                theString += cellArray[r][c] + " ";
                if (c % 3 == 2) {
                    theString += " | ";
                }

            }
            theString += "\n";
            if (r % 3 == 2) {
                theString += "--------------------------" + "\n";
            }

        }
        return theString;
    }

    public int getCols() {
        /**
         * returns the number of columns
         */
        return cellArray[0].length;
    }

    public int getRows() {
        /**
         * return number of rows
         */
        return cellArray.length;
    }

    public Cell get(int r, int c) {
        /**
         * return Cell at r,c
         */
        return cellArray[r][c];
    }

    public boolean isLocked(int r, int c) {
        /**
         * returns whether the Cell at r, c, is locked
         */
        return cellArray[r][c].isLocked();
    }

    public int numLocked() {
        /**
         * returns the number of locked Cells on the board
         */
        int numLocked = 0;
        for (int r = 0; r < cellArray.length; r++) { // what if did cellArray.length
            for (int c = 0; c < cellArray[r].length; c++) {
                if (cellArray[r][c].isLocked()) {
                    numLocked += 1;
                }
            }
        }
        return numLocked;
    }

    public int value(int r, int c) {
        /**
         * returns the value at Cell r, c.
         */
        return cellArray[r][c].getValue();
    }

    public void set(int r, int c, int value) {
        /**
         * sets the value of the Cell at r, c.
         */
        cellArray[r][c].setValue(value);
    }

    public void set(int r, int c, int value, boolean locked) {
        /**
         * sets the value and locked fields of the Cell at r, c.
         */
        cellArray[r][c].setLocked(locked);
        cellArray[r][c].setValue(value);

    }

    public boolean read(String filename) {
        /**
         * take in a file to read and have the board correspond to thsi file
         */
        try {
            // assign to a variable of type FileReader a new FileReader object, passing
            // filename to the constructor
            FileReader initalReader = new FileReader(filename);
            // assign to a variable of type BufferedReader a new BufferedReader, passing the
            // FileReader variable to the constructor
            BufferedReader initalBuffer = new BufferedReader(initalReader);
            // assign to a variable of type String line the result of calling the readLine
            // method of your BufferedReader object.
            String line = initalBuffer.readLine();
            // line.replaceAll(" ", "");
            // start a while loop that loops while line isn't null
            int linenum = 0;
            while (line != null) {
                line = line.trim();
                // assign to an array of type String the result of calling split on the line
                // with the argument "[ ]+"
                String[] StringArray = line.split("[ ]+");
                // print the String (line)

                // System.out.println(line); //teh actual word in the line
                // print the size of the String array (you can use .length)--number of columns
                for (int i = 0; i < StringArray.length; i++) {
                    set(linenum, i, Integer.parseInt(StringArray[i]));
                }
                // assign to line the result of calling the readLine method of your
                // BufferedReader object.
                line = initalBuffer.readLine();
                linenum++;
            }

            // call the close method of the BufferedReader
            initalBuffer.close();
            // return true
            return true;

        } catch (FileNotFoundException ex) {
            System.out.println("Board.read():: unable to open file " + filename);
        } catch (IOException ex) {
            System.out.println("Board.read():: error reading file " + filename);
        }

        return false;
    }

    public boolean validVlaue(int row, int col, int value) {
        /**
         * rteurn the possible valuet at teh given location
         */
        if (value > 0 && value < 10) {
            for (int i = 0; i < cellArray[row].length; i++) { // ceck columns within row
                if (cellArray[row][i].getValue() == value && i != col) {  //if number repeats in row
                    return false;
                }
            }

            for (int i = 0; i < cellArray.length; i++) { // check rows within columns
                if (cellArray[i][col].getValue() == value && i != row) {  //if number repeats in column
                    return false;
                }
            }

            int upperLeftRow = (row / 3) * 3;
            int upperLeftColumn = (col / 3) * 3;
            for (int r = upperLeftRow; r < upperLeftRow + 3; r++) {
                for (int c = upperLeftColumn; c < upperLeftColumn + 3; c++) {
                    if (cellArray[r][c].getValue() == value && (r != row && c != col)) {
                        return false;
                    }
                }

            }
            return true;
        }
        return false;
    }

    public boolean validSolution() {
        /**
         * return if a cell has a valid solution, goes through all cells
         */
        for (int r = 0; r < cellArray.length; r++) {
            for (int c = 0; c < cellArray[r].length; c++) {
                if (!validVlaue(r, c, cellArray[r][c].getValue())) {
                    return false;
                }
            }

        }
        return true;
    }

    public Cell findBestCell() {
        /**
         * if there is a cell with a value of 0, then create a new cell at that row and
         * column with a valid value
         */
        for (int initalRow = 0; initalRow < cellArray.length; initalRow++) {
            for (int initalColumn = 0; initalColumn < cellArray[initalRow].length; initalColumn++) {
                if (cellArray[initalRow][initalColumn].getValue() == 0) {
                    for (int value = 0; value < 10; value++) {
                        if (validVlaue(initalRow, initalColumn, value)) {
                            return new Cell(initalRow, initalColumn, value);
                        }

                    }
                    return null;
                }
            }
        }
        return null;
    }

    public void draw(Graphics g, int scale) {
        /**
         * actually draw the sudoku board
         */

        for (int r = 0; r < cellArray.length; r++) {
            for (int c = 0; c < cellArray[r].length; c++) {
                cellArray[r][c].draw(g, c, r, scale);
            }
        }
        for (int r = 1; r < 3; r++) {
            Graphics2D g2 = (Graphics2D) g;
            g2.setStroke(new BasicStroke(3));
            g2.setColor(Color.red);
            g2.drawLine(0, 3 * r * scale, 9 * scale, 3 * r * scale);
        }
        g.setColor(Color.GREEN);
        g.setFont(new Font("Arial", Font.PLAIN, 25));
        g.drawString("Sudoku game!", 80, 300);
        for (int c = 1; c < 3; c++) {
            Graphics2D g2 = (Graphics2D) g;
            g2.setStroke(new BasicStroke(3));
            g2.setColor(Color.blue);
            g2.drawLine(3 * c * scale, 0, 3 * c * scale, 9 * scale);
        }
    }

    public static void main(String[] args) {
        /**
         * test the baordtwo class
         */
        BoardTwo myBoard = new BoardTwo();
        System.out.println(myBoard.toString());
        System.out.println("# of columns:" + myBoard.getCols());
        System.out.println("# of rows:" + myBoard.getRows());
        System.out.println("cell at 3,4:" + myBoard.get(3, 4));
        System.out.println("is locked at 3,4?:" + myBoard.isLocked(3, 4));
        System.out.println("number of locked cells:" + myBoard.numLocked());
        System.out.println("cell value at 3,4:" + myBoard.value(3, 4));
        myBoard.set(3, 4, 1);
        System.out.println("cell at 3,4:" + myBoard.get(3, 4));
        myBoard.set(3, 4, 9, true);
        System.out.println("cell at 3,4:" + myBoard.get(3, 4));
        System.out.println("is locked at 3,4?:" + myBoard.isLocked(3, 4));
        System.out.println("number of locked cells:" + myBoard.numLocked());
        System.out.println(myBoard.toString());
        myBoard.read(args[0]);
        System.out.println(myBoard.toString());

        System.out.println(myBoard.validVlaue(8, 5, 8));
        myBoard.read(args[0]);
        System.out.println(myBoard.toString());
        System.out.println("second " + myBoard.validSolution());

    }
}
