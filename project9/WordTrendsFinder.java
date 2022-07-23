/**
 * Harsha Somaya
 * 04/19/2022
 * Section Lab C/D
 * Project 9
 * CS 231
 * WordTrendsFinder.java
 */
import java.util.Comparator;

public class WordTrendsFinder {
    private Comparator<String> comp;
    private WordCounter2 wordCounter;

    public WordTrendsFinder(Comparator<String> comparator) {
        /**
         * constructor for word trends finder
         */
        comp = comparator;
        wordCounter = new WordCounter2("bst", comp);
    }

    public double frequencyTracker(String filename, String word) {
        /**
         * return frequency of a word in a given word count file 
         */
        wordCounter.readWordCount(filename);
        // System.out.println("y: "+wordCounter.getMap().entrySet());
        double output=wordCounter.getFrequency(word);
        // System.out.println("here "+output);
        return output;
    }

    public static void main(String[] args) {
        /**
         * main method for testing through every file and args from command line
         */
        WordTrendsFinder test = new WordTrendsFinder(new AscendingString());
        String BaseFileName = args[0]; /// 2008analuzed
        Integer FileNumberBegin = Integer.parseInt(args[1]); //2008
        Integer FileNumberEnd = Integer.parseInt(args[2]);   //2015
        Double[][] matrix = new Double[FileNumberEnd - FileNumberBegin+1][args.length - 3]; // rows represent years,  //how is size correct
                                                                                          // column represent word
        for (int i = 0; i <= FileNumberEnd - FileNumberBegin; i++) {  //[0,7]-  0 1 2 3 4 5 6 7
            for (int j = 0; j < args.length-3 ; j++) {  //analyze this word for this file
                double output = test.frequencyTracker(BaseFileName, args[j+3]);

                matrix[i][j] = output;
            }
            BaseFileName = String.valueOf(FileNumberBegin + i) + "analyzed";      //go to next year
        }

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j]+"           ");  //after it has gone through all of the js, representing a column within a row
            }
            System.out.println();  //add a new line after a row

        }
    }
}
