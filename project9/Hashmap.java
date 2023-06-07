/**
 * Harsha Somaya
 * 04/05/2022
 * Section Lab C/D
 * Project 8
 * CS 231
 * Hashmap.java
 */

import java.util.Comparator;
import java.util.ArrayList;

public class Hashmap<K, V> implements MapSet<K, V> {
    private final Comparator<K> comparator;
    private int capacity;
    private int numCollisions;
    private MyDoublyLinkedList<KeyValuePair<K, V>>[] hashMap;
    private int size;

    public Hashmap(Comparator<K> incomp) { 
        /**Hashmap constructor that starts with default size hash table */
        comparator = incomp;
        capacity = 50;
        size = 0;
        hashMap = new MyDoublyLinkedList[capacity];
    }

    public Hashmap(Comparator<K> incomp, int capacity) { 
        /*Hashmap constructor that starts with the suggecsted capacity hash table
        */
        comparator = incomp;
        this.capacity = capacity;
        size = 0;
        hashMap = new MyDoublyLinkedList[capacity];

    }

   

    public boolean containsKey(K key) {
        /**
         * returns true if the map already contains a node with the specified key.
         */
        if (size == 0) { // if empty can not conatin a key
            return false;
        }
        int keyIndex = Math.abs(key.hashCode()); // turns memory location into a number
        keyIndex = keyIndex % capacity;
        if (hashMap[keyIndex] != null) {
            for (KeyValuePair<K, V> pair : hashMap[keyIndex]) {
                if (comparator.compare(pair.getKey(), key) == 0) {
                    return true;
                }

            }
        }
        return false;
    }

    public int size() {
        /**
         * return size of map
         */
        return size;
    }

    public int getCollisions(){
        /**
         * return number collisions
         */
        return numCollisions;
    }

    public V put(K key, V value) {
        /**
         * adds or updates a key-value pair.
         */
        int keyIndex = Math.abs(key.hashCode()); // turns memory location (@6 number string) into a number
        keyIndex = keyIndex % capacity;
        // System.out.println(keyIndex + " is the key index for " + key);

        if (1.0 * size() / capacity >= .85) {
            // System.out.println("expanidn");
            expand();
        }

        if (hashMap[keyIndex] != null) { // if something already at this index
            numCollisions++;
            if (containsKey(key)) { // no dupcate keys allowed, so update the key's value
                for (KeyValuePair<K, V> pair : hashMap[keyIndex]) { // for every pair in this linked list
                    if (comparator.compare(pair.getKey(), key) == 0) {
                        V oldValue = pair.getValue();
                        pair.setValue(value);
                        return oldValue;
                    }
                }
            }

            // already something at this index/linkedlist, but this is a unqiue key
            hashMap[keyIndex].addLast(new KeyValuePair<K, V>(key, value));
            size++;
            return null;
            //
        }

        // this is the first item @ keyIndex
        // System.out.println("making a  neww list @ " + keyIndex);
        KeyValuePair<K, V> pair = new KeyValuePair<K, V>(key, value);
        MyDoublyLinkedList<KeyValuePair<K, V>> addedList = new MyDoublyLinkedList<KeyValuePair<K, V>>(); // new list
        addedList.addFirst(pair); // add pair to list
        hashMap[keyIndex] = addedList; // add list with pair to map
        size++;
        return null;

    }

    public void expand() {
        /**
         * expands teh hash table to be double
         */
        System.out.println("Turning " + capacity + " into "+2*capacity);
        MyDoublyLinkedList<KeyValuePair<K, V>>[] expandedMap = new MyDoublyLinkedList[2 * capacity];
        ArrayList<KeyValuePair<K, V>> entryList = entrySet();
        hashMap = expandedMap;
        capacity = 2 * capacity;
        size = 0;
        numCollisions=0;
        for (KeyValuePair<K, V> pair : entryList) {
            put(pair.getKey(), pair.getValue());
        } System.out.println("Done expanding");
    }

    public ArrayList<K> keySet() {
        /**
         * returns an ArrayList that contains all of the keys in the map.
         */
        ArrayList<K> keyList = new ArrayList<K>();
        for (int i = 0; i < hashMap.length; i++) { // every linked list
            if (hashMap[i] != null) {
                for (KeyValuePair<K, V> pair : hashMap[i]) { // for every pair in this linked list
                    keyList.add(pair.getKey());
                }
            }
        }
        return keyList;
    }

    public ArrayList<V> values() {
        /**
         * return all the values
         */
        ArrayList<V> valueList = new ArrayList<V>();
        for (int i = 0; i < hashMap.length; i++) { // every linked list
            if (hashMap[i] != null) {
                for (KeyValuePair<K, V> pair : hashMap[i]) { // for every pair in this linked list

                    valueList.add(pair.getValue());
                }
            }
        }
        return valueList;

    }

    public void clear() {
        /**
         * clear hasmap
         */
        hashMap = new MyDoublyLinkedList[capacity];
        size = 0;

    }

    public ArrayList<KeyValuePair<K, V>> entrySet() {
        /**
         * returns an ArrayList that contains all of the pairs in the map.
         */
        ArrayList<KeyValuePair<K, V>> entryList = new ArrayList<KeyValuePair<K, V>>();
        for (int i = 0; i < hashMap.length; i++) { // every linked list
            if (hashMap[i] != null) {
                for (KeyValuePair<K, V> pair : hashMap[i]) { // for every pair in this linked list
                    entryList.add(pair);
                }
            }
        }
        return entryList;
    }

    public V get(K key) {
        /**
         * return value at this key if it exists
         */
        if (!containsKey(key)) {
            return null;
        }
        int keyIndex = Math.abs(key.hashCode()); // turns memory location (@6 number string) into a number
        keyIndex = keyIndex % capacity;
        if (hashMap[keyIndex] != null) {
            for (KeyValuePair<K, V> pair : hashMap[keyIndex]) { // for every pair in this linked list
                if (comparator.compare(pair.getKey(), key) == 0) {
                    return pair.getValue();
                }
            }
        }
        return null;  //maybe change to 0

    }

    public static void main(String[] args) {
        /**
         * main method for testing
         */
        Hashmap<String, Integer> test = new Hashmap<String, Integer>(new AscendingString(), 3);
        test.put("four", 4);
        test.put("seven", 7);
        test.put("eight", 8);
        test.put("four", 5); // this should be replace value 4 with 5
        test.put("six", 6);

        System.out.println("num collisions " + test.getCollisions());
        System.out.println(test.size());
        System.out.println(test.keySet());
        System.out.println(test.entrySet());
        System.out.println(test.values());
        System.out.println("should be 7 " + test.get("seven"));
        test.clear();
        System.out.println(test.size());

    }

}
