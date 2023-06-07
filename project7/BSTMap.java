
/**
 * Harsha Somaya
 * 04/05/2022
 * Section Lab C/D
 * Project 7
 * CS 231
 * BSTMap.java
 */

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class BSTMap<K, V> implements MapSet<K, V> {
        private TNode root;
        private int size;
        private Comparator<K> comparator;

        public BSTMap(Comparator<K> comp) {
                // constructor: takes in a Comparator object
                root = null;
                size = 0;
                comparator = comp;
        }

        public boolean containsKey(K key) {
                /**
                 * returns true if the map already contains a node with the specified key.
                 */
                if (root == null) { // if empty can not conatin a key
                        return false;
                }
                if (root.get(key, comparator) != null) {
                        return true; // contains jey
                }

                else {
                        return false;
                }

        }

        public V put(K key, V value) {
                /**
                 * adds or updates a key-value pair.
                 */
                if (root != null) { // if not empty
                        return root.put(key, value, comparator);
                } else { // empty
                        root = new TNode(key, value);
                        size++;
                        return null;
                }
        }

        public V get(K key) {
                /**
                 * call the root node's get method and
                 * gets the value at the specified key or null
                 */
                return root.get(key, comparator);
        }

        public int size() {
                /**
                 * return binary tree size
                 */
                return size;
        }

        public void clear() {
                /**
                 * clear the tree
                 */
                size = 0;
                root = null;

        }

        public ArrayList<K> keySet() {
                /**
                 * eturns an ArrayList that contains all of the keys in the map.
                 */
                ArrayList<K> keyList = new ArrayList<K>();
                return keySetRunner(root, keyList);
        }

        public ArrayList<K> keySetRunner(TNode root, ArrayList<K> keyList) {
                /**
                 * recursive function for keys being added to an array list
                 */
                if (root != null) {
                        // System.out.println(root.getKey());
                        keyList.add(root.getKey());
                        ArrayList<K> keyListLeft = keySetRunner(root.left, keyList);
                        return keySetRunner(root.right, keyListLeft);
                }
                return keyList;
        }

        public ArrayList<V> values() {
                /**
                 * returns an ArrayList that contains all of the values in the map.
                 */
                ArrayList<V> valueList = new ArrayList<V>();
                return valueSetRunner(root, valueList);
        }

        public ArrayList<V> valueSetRunner(TNode root, ArrayList<V> valuesList) {
                /**
                 * recursive function for values
                 */
                if (root != null) {
                        // System.out.println(root.getValue());
                        valuesList.add(root.getValue());
                        ArrayList<V> valueListLeft = valueSetRunner(root.left, valuesList);
                        return valueSetRunner(root.right, valueListLeft);
                }
                return valuesList;
        }

        public ArrayList<KeyValuePair<K, V>> entrySet() {
                /**
                 * returns an ArrayList of KeyValuePair objects.
                 */
                ArrayList<KeyValuePair<K, V>> entryList = new ArrayList<KeyValuePair<K, V>>();
                return entrySetRunner(root, entryList);
        }

        public ArrayList<KeyValuePair<K, V>> entrySetRunner(TNode root, ArrayList<KeyValuePair<K, V>> entryList) {
                /**
                 * recursive function for keys,values being added to an array list
                 */
                if (root != null) {
                        entryList.add(root.pair);
                        ArrayList<KeyValuePair<K, V>> pairListLeft = entrySetRunner(root.left, entryList);
                        return entrySetRunner(root.right, pairListLeft);
                }
                return entryList;
        }

        public String toString() {
                /**
                 * make teh bst map to a string
                 */
                return toStringRunner(root, "root ", 1);
        }

        public String toStringRunner(TNode root, String direction, int depth) {
                /**
                 * recursive for string runner
                 */
                if (root == null) {// empty
                        return "";
                }
                String output = direction + "\t" + "  ".repeat(depth) + root.pair + "\n"; // \t is for tab
                String leftString = toStringRunner(root.left, "left", depth + 1);
                String rightString = toStringRunner(root.right, "right", depth + 1);
                return output + leftString + rightString;

        }

        public ArrayList<K> mostCommon(int numberKeys){
                /**
                 * return the argument # of most common keys
                 */
                ArrayList<Integer> valueList= (ArrayList<Integer>) values();
                ArrayList<K> mostCommon= new ArrayList<>();
                ArrayList<K> keyList= keySet();
                int count=0;
                while (count<numberKeys){
                        Integer common=Collections.max(valueList);
                        int index=valueList.indexOf(common);

                        mostCommon.add(keyList.get(index));
                        keyList.remove(index);
                        valueList.remove(index);
                        count++;
                }
                return mostCommon;
        }
        

        private class TNode {
                // fields for the left and right children
                private TNode left;
                private TNode right;
                private KeyValuePair<K, V> pair;

                public TNode(K k, V v) {
                        // constructor, given a key and a value
                        // initialize all of the TNode fields
                        left = null;
                        pair = new KeyValuePair<K, V>(k, v);
                        right = null;

                }

                public V put(K key, V value, Comparator<K> comp) {
                        /**
                         * Takes in a key, a value, and a comparator and inserts
                         * the TNode in the subtree rooted at this node
                         * Returns the value associated with the key in the subtree
                         * or null if the key does not already exist
                         */

                        K currentKey = pair.getKey();
                        if (comp.compare(currentKey, key) > 0) { // current key is greater than key, go left
                                if (left != null) {
                                        left.put(key, value, comp);

                                } else { // eventually the left is null, menaing there is an open spot to put in the
                                         // node
                                        left = new TNode(key, value);
                                        size++;

                                }

                        } else if (comp.compare(currentKey, key) < 0) { // curent key is less than key, go right
                                if (right != null) {
                                        right.put(key, value, comp);
                                }

                                else { /// open spot, add there
                                        right = new TNode(key, value);
                                        size++;
                                }
                        }

                        else if (comp.compare(currentKey, key) == 0) { // already this key in tree
                                V oldValue = pair.getValue();
                                pair.setValue(value); // update existing key pair
                                return oldValue;

                        }
                        return null;
                }

                public V get(K key, Comparator<K> comp) {
                        /**
                         * Takes in a key and a comparator
                         * Returns the value associated with the key, recursng until it lands at that
                         * key, or null
                         */
                        K currentKey = pair.getKey();
                        if (comp.compare(currentKey, key) > 0) { // current key is greater than key, go left
                                if (left != null) { // what s this point
                                        return left.get(key, comp);
                                }
                        }

                        else if (comp.compare(currentKey, key) < 0) { // curent key is less than key, go right
                                if (right != null) {
                                        return right.get(key, comp);
                                }
                        }

                        else if (comp.compare(currentKey, key) == 0) { // key exissts,
                                return pair.getValue();
                        }

                        return null; // goes here if inner codition is not meant
                }

                public K getKey() {
                        /**
                         * return key
                         */
                        return pair.getKey();
                }

                public V getValue() {
                        /**
                         * return value
                         */
                        return pair.getValue();
                }

        }

        public static void main(String[] argv) {
                /*
                 * test, create a BSTMap
                 */
                BSTMap<String, Integer> bst = new BSTMap<>(new AscendingString());
                bst.put("twenty", 20);
                bst.put("ten", 10);
                bst.put("eleven", 11);
                bst.put("five", 5);
                bst.put("six", 6);
                System.out.println(bst.get("eleven"));
                System.out.println("shoudl be false: " + bst.containsKey("ff"));
                System.out.println("shoudl be true: " + bst.containsKey("five"));
                System.out.println("should be 5 " + bst.size());
                System.out.println(bst.keySet());
                System.out.println(bst.values());
                System.out.println(bst.entrySet());
                System.out.println(bst);
                bst.clear();
                System.out.println("should be 0 " + bst.size);

        }

}