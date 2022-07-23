/**
 * Harsha Somaya
 * 04/05/2022
 * Section Lab C/D
 * Project 7
 * CS 231
 * WordCounter.java
 */

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.io.*;

public class WordCounter {
    private int totalWordCount;
    private BSTMap<String, Integer> bstMap;

    public WordCounter() {
        /**
         * constructor that makes an empty BSTMap and sets the total word count to zero.
         */
        bstMap = new BSTMap<>(new AscendingString()); // maybe add in <>
        totalWordCount = 0;
    }

    public void analyze(String filename) {
        /**
         * makes a bst from a given file 
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
            while (line != null) {             // start a while loop that loops while line isn't null
                line = line.trim(); /// get ride of trailing and leading spaces
                // assign to an array of type String the result of calling split on the line
                String[] StringArray = line.split("[^a-zA-Z0-9']"); // line becomes an array of spearated words
                // System.out.println(line); //teh actual word in the line
                for (int i = 0; i < StringArray.length; i++) { // for every word in the word array of words in a single line
                    String word = StringArray[i].trim().toLowerCase(); // make every word lowercase
                    if (word.length() != 0) { //if there is a word
                        totalWordCount++;
                        if (bstMap.containsKey(word)) {  //if the word is alread on the map
                            bstMap.put(word, bstMap.get(word) + 1);   //update the map with bstMpa.put(word, value at word   +1 because increasing its value)
                        } else {
                            bstMap.put(word, 1);
                        }
                    }

                }

                line = initalBuffer.readLine();  //goes to next line
            
            }
            // call the close method of the BufferedReader
            initalBuffer.close();
        } catch (FileNotFoundException ex) {
            System.out.println("Board.read():: unable to open file " + filename);
        } catch (IOException ex) {
            System.out.println("Board.read():: error reading file " + filename);
        }

    }

    public int getTotalWordCount() {
        /**
         * returns the total word count --- all values added together
         */
        return totalWordCount;
    }

    public int getUniqueWordCount() {
        /**
         * returns the number of unique words, which should be the size of the BSTMap.  or the number of keys
         */
        return bstMap.size();
    }

    public int getCount(String word) {
        /**
         * returns the frequency value associated with this word.
         */
        return bstMap.get(word);
    }

    public double getFrequency(String word) {
        /**
         * returns the value associated with this word divided by the total word count.
         */
        return (float) bstMap.get(word) / totalWordCount;

    }

    public String toString() {
        /**
         * return the bst map toString
         */
        return bstMap.toString();
    }



    public void writeWordCountFile(String filename) {
        /**
         * writes the contents of the BSTMap to a word count file.
         */
        try {
            String output = "totalWordCount : " + totalWordCount + "\n";
            ArrayList<KeyValuePair<String, Integer>> array = bstMap.entrySet();
            for (KeyValuePair<String, Integer> element : array) {
                output += element + "\n";  //create the string  ///TO STirng utomatyically tSTring

            }
            File newFile = new File(filename);  ///makes a new file with the given name
            newFile.createNewFile();
            FileWriter writer = new FileWriter(newFile);
            writer.write(output);  ///add to this  string to teh file 
            writer.flush();
            writer.close();

        } catch (FileNotFoundException ex) {
            System.out.println("Board.read():: unable to open file " + filename);
        } catch (IOException ex) {
            System.out.println("Board.read():: error reading file " + filename);
        }
    }

    public void readWordCountFile( String filename ){
         /**
         * reads the contents of a word count file and reconstructs the fields of the WordCount object, including the BSTMap.
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
            BSTMap<String, Integer> secondBst = new BSTMap<>(new AscendingString());
            line = initalBuffer.readLine();

            while (line != null) {             // start a while loop that loops while line isn't null
                line = line.trim(); /// get ride of trailing and leading spaces
                // assign to an array of type String the result of calling split on the line
                // with the argument "[ ]+"
                String[] StringArray = line.split("[^a-zA-Z0-9']"); // line becomes an array of spearated words
                // System.out.println(line); //teh actual word in the line
                for (int i = 0; i < StringArray.length; i++) { // for every word in the word array. 
                    String key=StringArray[2].trim().toLowerCase(); // make every word lowercase, and get the key
                    secondBst.put(key, Integer.parseInt(StringArray[6].trim().toLowerCase())); //update teh second BST, no need to update values because the given file already has it analyzed
                    }
                line = initalBuffer.readLine();
                }
                    
                bstMap=secondBst;
            // call the close method of the BufferedReader
            initalBuffer.close();
        } catch (FileNotFoundException ex) {
            System.out.println("Board.read():: unable to open file " + filename);
        } catch (IOException ex) {
            System.out.println("Board.read():: error reading file " + filename);
        } 
    }

    public ArrayList<String> mostCommon(int numberKeys){
        /**
         * return the most common keys for this bstMap
         */
        return (ArrayList<String>)bstMap.mostCommon(numberKeys);
    }


    public static void main(String[] args) {
        /**
         * test the WordCounter
         */
        WordCounter wordCountTest = new WordCounter();
        System.out.println(wordCountTest);
        long before=System.currentTimeMillis();
        wordCountTest.analyze(args[0]); 
        long after=System.currentTimeMillis();
        System.out.println("run time difference: "+(after-before));
        wordCountTest.writeWordCountFile(args[1]);
        wordCountTest.readWordCountFile(args[1]);
        System.out.println("unique: "+wordCountTest.getUniqueWordCount());
        System.out.println("total: "+wordCountTest.getTotalWordCount());
        System.out.println("top keys: "+wordCountTest.mostCommon(20));
        System.out.println(wordCountTest);
        //System.out.println(wordCountTest.getFrequency("the"));
       // System.out.println(wordCountTest.getCount("the"));



    }

}
