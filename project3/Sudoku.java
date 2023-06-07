
/**
 * Sudoku.java
 * Actually solve the sudoku game 
 * Harsha Somaya
 * CS231 S22
 * Project 3/4
 * 3/7/2022
 * Lab C/D
 */
import java.util.Random;

public class Sudoku {
    /**
     * declare the actual board and landscae disay
     */
    private BoardTwo board;
    private LandscapeDisplay display;

    public Sudoku() {
        /**
         * constructor for sudoku board if no intial random values given
         */
        board = new BoardTwo();
        display = new LandscapeDisplay(board, 30);
    }

    public Sudoku(int numN) {
        /**
         * create a sudokou board with numN random values
         */
        board = new BoardTwo();
        Random r = new Random();
        int i = 0;
        display = new LandscapeDisplay(board, 30);
        while (i <= numN) {
            int row = r.nextInt(9); // retrun row between 0 and 8
            int column = r.nextInt(9);// return columb b/w 0and 8
            int value = r.nextInt(9) + 1; // [0,8]+1=[1,9]
            if (board.get(row, column).getValue() != 0) {
                continue;  
            } else if (board.get(row, column).getValue() == 0) {
                if (board.validVlaue(row, column, value)) {
                    board.set(row, column, value, true); // add and make locked
                    i++;
                } else {
                    continue;
                }
            }
        }
    }

    public boolean solve(int delay) {
        /**
         * solve the sudoku board, returning boolean
         */
        CellStack stack = new CellStack();
        int unLocked = board.getRows() * board.getCols() - board.numLocked();
        boolean toBreak = false;

        while (stack.size() < unLocked) {  //ends up here after braking   //less tan unlocked because can only alter unlocked, and stack is first emty until it has added all the unlocked cells
            if (delay > 0) {
                try {
                    Thread.sleep(delay);
                } catch (InterruptedException ex) {
                    System.out.println("Interrupted");
                }
                display.repaint();
            }
            Cell nextCell = board.findBestCell();
            // System.out.println("finidng next cell");
            if (nextCell != null) {
                stack.push(nextCell);
                // System.out.println("push cell to stack");
                board.set(nextCell.getRow(), nextCell.getCol(), nextCell.getValue());
            } else {
                // System.out.println("null, no valid values");
                while (!stack.empty()) {   
                    Cell cellPopped = stack.pop();  //old cells, backtracking
                    // System.out.println("pop from stack");
                    for (int value = cellPopped.getValue() + 1; value < 10; value++) {
                        if (board.validVlaue(cellPopped.getRow(), cellPopped.getCol(), value)) {
                            cellPopped.setValue(value);
                            stack.push(cellPopped);
                            // System.out.println("found new value");
                            board.set(cellPopped.getRow(), cellPopped.getCol(), value);
                            toBreak = true;
                            break;
                        }
                    }

                    if (toBreak) {
                        toBreak = false;
                        break;
                    }

                    if (!toBreak) {
                        cellPopped.setValue(0);
                        board.set(cellPopped.getRow(), cellPopped.getCol(), 0); // goes to while because value woudl
                                                                                // have gone till 9 and checked in if
                                                                                // staemnet
                    }
                    if (stack.empty()) {
                        return false;
                    }
                }
            }
        }
        return true;

    }

    public static void main(String[] args) {
        /**
         * test teh Sudoku class
         */
        Sudoku trial = new Sudoku(20);
        //trial.board.read(args[0]);
        System.out.println("inital");
        System.out.println(trial.board);
        boolean output=trial.solve(10);
        System.out.println(trial.board);
        System.out.println("o is: "+output);
        // Sudoku trial = new Sudoku(0);
        // System.out.println("inital board");
        // System.out.println(trial.solve());
        // System.out.println("final board");
        // System.out.println(trial.board);

    }
}
