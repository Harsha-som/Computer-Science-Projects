import java.io.*;

public class Board {
    public boolean read(String filename) {
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
            // start a while loop that loops while line isn't null
            while (line != null) {
                // assign to an array of type String the result of calling split on the line
                // with the argument "[ ]+"
                String[] StringArray = line.split("[ ]+");
                // print the String (line)
                System.out.println(line);
                // print the size of the String array (you can use .length)
                System.out.println(StringArray.length);
                // assign to line the result of calling the readLine method of your
                // BufferedReader object.
                line = initalBuffer.readLine();
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
    public static void main(String[] args) {
        Board myBoard= new Board();
        myBoard.read(args[0]);
    }
}
