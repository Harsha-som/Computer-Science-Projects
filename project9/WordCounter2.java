/**
 * Harsha Somaya
 * 04/05/2022
 * Section Lab C/D
 * Project 9
 * CS 231
 * WordCounter2.java
 */

import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.*;
import java.util.Collections;
import java.util.Comparator;

public class WordCounter2 {
    private MapSet map;
    private int totalWordCount;
    private int unqiueWordCount;

    
    public WordCounter2(MapSet map){
        /**
         * constructor for when i pass in an actual map
         */
        this.map=map;
    }

    public WordCounter2(String data_structure) {
        /**
         * constructor, where data_structure is either "bst" or "hashmap"
         */
        if (data_structure.equals("bst")) {
            map = new BSTMap<String, Double>(new AscendingString());
            totalWordCount = 0;
        } else if (data_structure.equals("hashmap")) {
            map = new Hashmap<String, Double>(new AscendingString());
            totalWordCount = 0;
        }
    }

    
    public WordCounter2(String data_structure, Comparator<String> comp) {
        /**
         * constructor, where data_structure is either "bst" or "hashmap"
         */
        if (data_structure.equals("bst")) {
            map = new BSTMap<String, Double>(comp);
            totalWordCount = 0;
        } else if (data_structure.equals("hashmap")) {
            map = new Hashmap<String, Double>(comp);
            totalWordCount = 0;
        }
    }

    public ArrayList<String> readWords(String filename) {
        /**
         * given the filename of a text file, read the text file and return an ArrayList
         * list of all the words in the file.
         */
        ArrayList wordList = new ArrayList<>();
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
            while (line != null) { // start a while loop that loops while line isn't null
                line = line.trim(); /// get ride of trailing and leading spaces
                // assign to an array of type String the result of calling split on the line
                String[] StringArray = line.split("[^a-zA-Z0-9']"); // line becomes an array of spearated words
                // System.out.println(line); //teh actual word in the line
                for (int i = 0; i < StringArray.length; i++) { // for every word in the word array of words in a single
                                                               // line
                    String word = StringArray[i].trim().toLowerCase(); // make every word lowercase
                    if (word.length()!=0){
                        wordList.add(word);
                        totalWordCount++;
                    }
                }

                line = initalBuffer.readLine(); // goes to next line

            }
            // call the close method of the BufferedReader
            initalBuffer.close();
        } catch (FileNotFoundException ex) {
            System.out.println("Board.read():: unable to open file " + filename);
        } catch (IOException ex) {
            System.out.println("Board.read():: error reading file " + filename);
        }
        return wordList;
    }

    public double buildMap(ArrayList<String> words) {
        /**
         * given an ArrayList of words, put the words into the map data structure.
         */
        double before = System.nanoTime();
        double processed = 0;
        double threshold = 1;
        for (String word : words) {

            if (map.containsKey(word)) {
                map.put(word, (int) map.get(word) + 1);
            } else {
                map.put(word, 1);
                unqiueWordCount++;
            }
            processed += 1;
            if (processed / words.size() * 100 > threshold){
                System.out.println(""  + threshold + "%");
                threshold++;
            }
        }
        return System.nanoTime() - before;
    }

    public void clearMap() {
        /**
         * clear the map data structure
         */
        map.clear();
        totalWordCount=0;
        unqiueWordCount=0;
    }

    public int getTotalWordCount() {
        /**
         * return total word count from last time readWords was called
         */
        return totalWordCount;
    }

    public int getUniqueWordCount() {
        /**
         * return the unique word count, which should be the size of the map data
         * structure.
         */
        return unqiueWordCount;
    }

    public int getCount(String word) {
        /**
         * return the number of times the word occurred in the list of words.
         */

        if (!map.containsKey(word)) {
            return 0;
        }
        return (int) map.get(word);
    }

    public double getFrequency(String word) {
        /**
         * return the frequency of the word in the list of words.
         */
        if (map.containsKey(word) == false) {
            return 0;
        }
        return (double) getCount(word) /(double) totalWordCount;
    }

    public boolean writeWordCount(String filename) {
        /**
         * write a word count file given the current set of words in the data structue
         */
        try {
            String output = "totalWordCount : " + totalWordCount + "\n";
            ArrayList<KeyValuePair<String, Integer>> array = map.entrySet();

            for (KeyValuePair<String, Integer> pair : array) {
                // pair.setValue((double)getFrequency(pair.getKey()));
                output += "key " + pair.getKey() + " : value " + getFrequency(pair.getKey()) + "\n"; // create the
            }
            File newFile = new File(filename); /// makes a new file with the given name
            newFile.createNewFile();
            FileWriter writer = new FileWriter(newFile);
            writer.write(output); /// add to this string to teh file
            writer.flush();
            writer.close();
            return true;

        } catch (FileNotFoundException ex) {
            System.out.println("Board.read():: unable to open file " + filename);
        } catch (IOException ex) {
            System.out.println("Board.read():: error reading file " + filename);
        }
        return false;
    }

    public boolean readWordCount(String filename) {
        /**
         * read a word count file given the filename
         */
        map.clear();
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
            line = initalBuffer.readLine();

            while (line != null) { // start a while loop that loops while line isn't null
                line = line.trim(); /// get ride of trailing and leading spaces
                // assign to an array of type String the result of calling split on the line
                String[] StringArray = line.split("[^a-zA-Z0-9.']"); // line becomes an array of spearated words
                // for (String string:StringArray){
                //     System.out.print(string+" ,");    
                // }

                // System.out.println();
                // System.out.println(line); //teh actual word in the line
                                                            // line
                // System.out.println("elemt in string arraay (values) \"" + StringArray[i] + "\"");
                String key = StringArray[2].trim().toLowerCase(); // make every word lowercase
                totalWordCount+=Integer.parseInt(StringArray[6].trim().toLowerCase());
                unqiueWordCount+=1;
                map.put(key, Integer.parseInt(StringArray[6].trim().toLowerCase()));
                line = initalBuffer.readLine(); // goes to next line
            }
            // call the close method of the BufferedReader
            initalBuffer.close();
            // System.out.print("wordocunter2 "+map.entrySet());
            return true;
        } catch (FileNotFoundException ex) {
            System.out.println("Board.read():: unable to open file " + filename);
        } catch (IOException ex) {
            System.out.println("Board.read():: error reading file " + filename);
        }
        return false;
    }

    public MapSet getMap(){
        return map;
    }

   

    public static void main(String[] args) {
        /**
         * main method for testting
         */

        Hashmap<String,Integer> map=new Hashmap<String,Integer>(new AscendingString());
        WordCounter2 test=new WordCounter2(map);
        ArrayList<Long> runTimes=new ArrayList<>(5);

        for (int i=0; i<5;i++){
            test.clearMap();
            long before=System.currentTimeMillis();
            System.out.println("Reading");
            ArrayList<String> list=test.readWords(args[0]);
            System.out.println("Done reading, now building");
            test.buildMap(list);
            System.out.println("Done building");
            runTimes.add(System.currentTimeMillis()-before);
        }

        for (int i=0; i<1;i++){ ///remove highest
            Long max=Collections.max(runTimes);
            runTimes.remove(max);
        }

        for (int i=0; i<1;i++){ ///remove lowest
            Long min=Collections.min(runTimes);
            runTimes.remove(min);
        }

        int sum=0;
        for (int i=0;i<runTimes.size();i++){
            sum+=runTimes.get(i);
        }
        System.out.println("number collsions: "+map.getCollisions());
        System.out.println("average run times: "+(sum/runTimes.size()));
        System.out.println(test.map.entrySet());
        // System.out.println("the depth is "+map.getMaxDepth());  --for bst maps only
        System.out.println("total word count: " +test.getTotalWordCount());
        System.out.println("unique word count "+test.getUniqueWordCount());
        System.out.println("count of the is "+test.getCount("the"));
        System.out.println("frequency "+ test.getFrequency("the"));
        // test.writeWordCount("count file analyzed.txt");   --when using dummy counttest file
        test.readWordCount("count file analyzed.txt");
        System.out.println(test.map.entrySet());
        test.clearMap();
        System.out.println(test.map.entrySet());
    }
}
