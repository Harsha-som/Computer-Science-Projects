/**
 * Harsha Somaya
 * 04/19/2022
 * Section Lab C/D
 * Project 9
 * CS 231
 * CommonWordsFinder.java
 */

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class CommonWordsFinder  {
    private PQHeap<KeyValuePair<String,Integer>> heap;
    private int totalWordCount;

    
    public CommonWordsFinder(){
        /**
         * constructor for commonwordsfiner
         */
        heap = new PQHeap <KeyValuePair<String,Integer>> (new KVTestComparatorTwo());
    }

    public void readWords(String filename) {
        /**
         * given the filename of a text file, read the text file and return an ArrayList
         * list of all the words in the file.
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
            String line = initalBuffer.readLine(); /// gives the first line
            line = initalBuffer.readLine(); /// gives the first line
            while (line != null) { // start a while loop that loops while line isn't null
                line = line.trim(); /// get ride of trailing and leading spaces
                // assign to an array of type String the result of calling split on the line
                String[] StringArray = line.split("[^a-zA-Z0-9']"); // line becomes an array of spearated words
                    // if (line.charAt(5)=='\''){
                    //     for (String element:StringArray){
                    //         System.out.print(element +" ");
                    //     }
                    //     System.out.print("\n");

                    // }
                    
                // System.out.println(line); //teh actual word in the line
                String key  = StringArray[2].trim().toLowerCase(); // make every word lowercase
                if (key.length()!=0){
                    KeyValuePair<String,Integer> pair= new KeyValuePair<String,Integer>(key, Integer.parseInt(StringArray[6].trim().toLowerCase()));
                    heap.add(pair);
                    totalWordCount+=pair.getValue();
                }
                line = initalBuffer.readLine(); // goes to next line
            }
            initalBuffer.close();         // call the close method of the BufferedReader
        } catch (FileNotFoundException ex) {
            System.out.println("Board.read():: unable to open file " + filename);
        } catch (IOException ex) {
            System.out.println("Board.read():: error reading file " + filename);
        }
    }

    private int getTotalWordCount(){
        /**
         * returns totalword count
         */
        return totalWordCount;
    }

    

    public static void main(String[] args) {
        /**
         * main method for getting word frequencies
         */
        CommonWordsFinder test=new CommonWordsFinder();
        System.out.println(test.heap);    
        for (int j=1;j<args.length;j++){  
            System.out.println(args[j]);  //shoudld prnt filena,e
            test.readWords(args[j]);//file name
            for (int i=0;i<Integer.parseInt(args[0]);i++){ //first word is x most cmmon
                System.out.println(test.heap.get(i)+" word frequency is "+((float)test.heap.get(i).getValue())/test.getTotalWordCount()); 
            }   
        }
    }

}
