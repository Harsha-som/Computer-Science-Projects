
/**
 * LinkedList.java
 * Harsha Somaya
 * CS231 S22
 * Project 5
 * 3/7/2022
 * Lab C/D
 */

import java.util.Iterator; // defines the Iterator interface
import java.util.ArrayList;
import java.util.Collections; // contains a shuffle function4

public class LinkedList<T> implements Iterable<T> {
    /**
     * link list class with fields
     */
    private int size;
    private Node head;

    public LinkedList() {
        /**
         * constructor that initializes the fields so it is an empty list.
         */
        size = 0;
        head = null;
    }

    public class Node {
        /**
         * inner class node and its field
         */
        private T data;
        private Node next;

        public Node(T item) {
            /**
             * constrcutor for node class
             */
            next = null;
            data = item;
        }

        public T getThing() {
            /**
             * returns the value of the container field.
             */
            return data;
        }

        public void setNext(Node n) {
            /**
             * sets next to the given node.
             */
            next = n;
        }

        public Node getNext() {
            /**
             * returns the next field
             */
            return next;
        }

        public Node getHead() {
            /**
             * returns head
             */
            return head;
        }

    }

  

    public void clear() {
        /**
         * empties the list (resets the fields so it is an empty list).
         */
        size = 0;
        head = null;
    }

    public int size() {
        /**
         * returns the size of the list.
         */
        return size;
    }

    public void add(int index, T item) {
        /**
         * inserts the item at the specified poistion in the list
         */
        Node newNode = new Node(item);
        if (size() != 0) {
            Node current = head;
            if (index == 0) {
                addFirst(item);
            } else {
                for (int i = 0; i < index - 1; i++) { // current is node before desired node
                    current = current.getNext();

                }
                Node afterNode = current.getNext();
                if (afterNode == null) {
                    current.setNext(newNode);
                    size++;

                } else {
                    current.setNext(newNode);
                    newNode.setNext(afterNode);
                    size++;
                }
            }
        } else {
            if (index == 0) {
                addFirst(item);
            }
        }
    }

    public T remove(int index) {
        /**
         * removes the item at the specified position in the list.
         */
        if (size() != 0 && index < size()) {
            Node current = head;
            if (index == 0) {
                head = head.getNext();
                size--;
                return current.getThing();
            }
            for (int i = 0; i < index - 1; i++) { // current is node before desired node
                current = current.getNext();

            }
            T nodeRemoved = current.getNext().getThing();
            current.setNext(current.getNext().getNext());
            size--;
            return nodeRemoved;
        }

        return null;

    }

    public Iterator<T> iterator() {
        /**
         * // Return a new LLIterator pointing to the head of the list
         */
        return new LLIterator(head);

    }

    private class LLIterator implements Iterator<T> {

        private Node nextNode;

        public LLIterator(Node head) {
            /**
             * the constructor for the LLIterator given the head of a list.
             */
            nextNode = head;
        }

        public T next() {
            /**
             * returns the next item in the list, which is the item contained in the current
             * node. The method also needs to move the traversal along to the next node in
             * the list.
             */
            if (hasNext()) {
                T data = nextNode.getThing();
                nextNode = nextNode.getNext();
                return data;
            } else {
                return null;
            }
        }

        public boolean hasNext() {
            /**
             * returns true if there are still values to traverse (if the current node
             * reference is not null).
             */
            if (nextNode != null) {
                return true;
            } else {
                return false;
            }
        }

    }

    public void addFirst(T item) {
        /**
         * inserts the item at the beginning of the list.
         */
        Node newNode = new Node(item);
        newNode.setNext(head);
        head = newNode;
        size++;
    }

    public void addLast(T item) {
        /**
         * appends the item at the end of the list.
         */
        Node newNode = new Node(item);
        Node current = head;
        if (size() != 0) {
            while (current.getNext() != null) {
                current = current.getNext();
            }
            current.setNext(newNode); // curent is node before null
            size++;
        } else {
            addFirst(item);
        }
    }

    public ArrayList<T> toArrayList() {
        /**
         * returns an ArrayList of the list contents in order.
         */
        ArrayList<T> arrayList = new ArrayList<>();
        Node current = head;
        for (int i = 0; i < size(); i++) {
            arrayList.add(current.getThing());
            current = current.getNext();
        }
        return arrayList;

    }

    public ArrayList<T> toShuffledList() {
        /**
         * returns an ArrayList of the list contents in shuffled order.
         */
        ArrayList<T> shuffled = toArrayList();
        Collections.shuffle(shuffled);
        return shuffled;

    }

    public static void main(String[] args) {
        LinkedList<Integer> ll = new LinkedList<>();
        System.out.println("shoudl be 0: " + ll.size());
        ll.addFirst(37);
        ll.addFirst(2);
        ll.addFirst(1);
        ll.addFirst(100);
        ll.remove(2);
        System.out.println("should be 3 " + ll.size());
        ll.clear();
        System.out.println("shoudl be 0: " + ll.size());
        ll.addLast(4);
        ll.add(0, 1);
        ll.add(1, 2);
        System.out.println("array list: "+ll.toArrayList());
        Iterator<Integer> iterator= ll.iterator(); 
        while(iterator.hasNext()) {
            int obj = (int)iterator.next();
            System.out.println(obj);
      }
        System.out.println(ll.toShuffledList());
    }
}
