/**
 * CellStack.java
 * Create a cell stack, where the top is last cell added
 * Harsha Somaya
 * CS231 S22
 * Project 3/4
 * 3/7/2022
 * Lab C/D
 */
public class CellStack {
    private Cell[] mystack;
    private int nextFreeSpot;

    public CellStack() {
        /**
         * initialize the stack to a default size.
         */
        mystack = new Cell[30];
        nextFreeSpot = 0; // initally nothing actually in cell, so next free spot at index 0
    }

    public CellStack(int max) {
        /**
         * itialize the stack to hold up to max elements.
         */
        mystack = new Cell[max];
        nextFreeSpot = 0;
    }

    public int size() {
        /**
         * return the number of selements on the stack
         */
        return nextFreeSpot;
    }

    public boolean empty() {
        /**
         * return true if the stack is empty
         */
        if (size() == 0) {
            return true;
        } else {
            return false;
        }
    }

    public Cell push(Cell c) {
        /**
         * if there is space, push c onto the stack.
         */
        if (size() == mystack.length) {
            Cell[] newArray = new Cell[2 * mystack.length];
            for (int i = 0; i < size(); i++) {
                newArray[i] = mystack[i];
            }
            mystack = newArray;
        }
        mystack[nextFreeSpot] = c;
        nextFreeSpot++;
        return c;
    }

    public Cell pop() {
        /**
         * remove and return the top element from the stack; return null if the stack is
         * empty.
         */
        if (empty()) {
            return null;
        } else {
            Cell cellPoped = mystack[nextFreeSpot - 1];
            mystack[nextFreeSpot - 1] = null;
            nextFreeSpot--;
            return cellPoped;
        }
    }

    public static void main(String[] args) {
        /**
         * test CellStack class
         */
        CellStack one = new CellStack();
        System.out.println(one.mystack[9]);

    }
}
