
/**
 * Sudoku.java
 * Reprresent a single cell
 * Harsha Somaya
 * CS231 S22
 * Project 3/4
 * 3/7/2022
 * Lab C/D
 */
import java.awt.Graphics;
import java.awt.BasicStroke;
import java.awt.Graphics2D;

public class Cell {
    /**
     * create class fr a single cell
     */
    private Integer rowIndex;
    private Integer columnIndex;
    private Integer value;
    private boolean isLocked;

    public Cell() {
        /**
         * constructor for teh class, inital state
         */
        rowIndex = 0;
        columnIndex = 0;
        value = 0;
        isLocked = false;
    }

    public Cell(int row, int col, int value) {
        /**
         * constructor two with given row, column, and value
         */
        rowIndex = row;
        columnIndex = col;
        this.value = value;
        isLocked = false;

    }

    public Cell(int row, int col, int value, boolean locked) {
        /**
         * constructor three with given row, column, value, and locked state
         */
        rowIndex = row;
        columnIndex = col;
        this.value = value;
        isLocked = locked;

    }

    public int getRow() {
        /**
         * return the Cell's row index
         */
        return rowIndex;
    }

    public int getCol() {
        /**
         * return the Cell's column index
         */
        return columnIndex;
    }

    public int getValue() {
        /**
         * return the Cell's value
         */
        return value;
    }

    public void setValue(int newval) {
        /**
         * set the Cell's value
         */
        value = newval;
    }

    public boolean isLocked() {
        /**
         * return the value of the locked field.
         */
        return isLocked;
    }

    public void setLocked(boolean lock) {
        /**
         * set the Cell's locked field to the new value
         */
        isLocked = lock;
    }

    public Cell clone() {
        /**
         * return a new Cell with the same values as the existing Cell.
         */
        return new Cell(rowIndex, columnIndex, value, isLocked);
    }

    public String toString() {
        /**
         * generate and return a representating String
         */
        // return "position: "+ rowIndex+", "+columnIndex+" value: "+value+" locked:
        // "+isLocked;
        return Integer.toString(value);
    }

    public void draw(Graphics g, int x0, int y0, int scale) {
        char[] charArray = { (char) ('0' + this.value), 0 };
        Graphics2D g2 = (Graphics2D) g;
        g2.setStroke(new BasicStroke(2));
        g2.drawChars(charArray, 0, 1, x0 * scale + 13, y0 * scale + 20);
        g2.drawRect((x0 + getCol()) * scale, (y0 + getRow()) * scale, scale, scale);
    }

    public static void main(String[] args) {
        /**
         * test the cell mehthod by creating a cell and cloning it
         */
        Cell firstcell = new Cell(4, 8, 9);
        Cell seconcell = firstcell.clone();
        System.out.println(seconcell);

    }
}
