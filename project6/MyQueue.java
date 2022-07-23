
/**
 * Harsha Somaya
 * 03/18/2022
 * Section Lab C/D
 * Project 6
 * CS 231
 * MyQueue.java
 */

import java.util.Iterator;

public class MyQueue<T> implements Iterable<T> {
    /**
     * fields for outer queue class
     */
    private int size;
    private Node<T> head;
    private Node<T> tail;

    public MyQueue() {
        /**
         * consructor for queue, orginally set fields to null or 0
         */
        size = 0;
        head = null;
        tail = null;
    }

    private class Node<T> {
        /**
         * inner node class with fields in every node
         */
        private T data;
        private Node<T> next;
        private Node<T> prev;

        public Node(T val, Node<T> next, Node<T> previous) {
            /**
             * constructor for node
             */
            data = val;
            this.next = next;
            prev = previous;
        }

        public T getData() {
            /**
             * returns data in node
             */
            return data;
        }

        public Node<T> getNext() {
            /**
             * return next refrence for a node
             */
            return next;
        }

        public void setNext(Node<T> n) {
            /**
             * set next field to argument n
             */
            next = n;
        }

        public Node<T> getPrev() {
            /**
             * return previous of a node
             */
            return prev;
        }

        public void setPrev(Node<T> n) {
            /**
             * set prev field to argument n
             * 
             */
            prev = n;
        }
    }

    public Iterator<T> iterator() {
        /**
         * abstract method reqiured in interaable outer queue class
         */
        return new MyLinkedListIterator(head);
    }

    public class MyLinkedListIterator implements Iterator<T> {
        /**
         * allows the iteration to take place
         */

        private Node<T> nextNode;

        public MyLinkedListIterator(Node<T> head) {
            /**
             * constructor for iterator class, first nextNode is head
             */
            nextNode = head;
        }

        public T next() {
            /**
             * give the nextNode data and then increment next
             */
            T data = nextNode.getData();
            nextNode = nextNode.getNext();
            return data;
        }

        public boolean hasNext() {
            /**
             * return true if there is a nextnode
             */
            if (nextNode != null) {
                return true;
            } else {
                return false;
            }
        }

    }

    public int size() {
        /**
         * Returns the number of elements in the stack.
         * 
         * @return number of elements in the stack
         */
        return size;
    }

    public boolean empty() {
        /**
         * Tests whether the stack is empty.
         * 
         * @return true if the stack is empty, false otherwise
         */
        if (size() == 0) {
            return true;
        } else {
            return false;
        }
    }

    public void clear() {
        /**
         * clear the queue
         */
        size = 0;
        head = null;
    }

    public boolean offer(T item) {
        /**
         * Inserts item into this queue if possible. Returns true if successful. adds to
         * end
         */
        Node<T> newNode = new Node<T>(item, null, tail);
        if (!empty()) {
            tail.setNext(newNode);
        } else {
            head = newNode;
        }
        size++;
        tail = newNode;
        return true;
    }

    public T peek() {
        /**
         * Returns, but does not remove, the head of this queue, or returns null if this
         * queue is empty.
         */
        if (empty()) {
            return null;
        } else {
            return head.getData();
        }
    }

    public T poll() {
        /**
         * Returns and removes the head of this queue, or returns null if this queue is
         * empty
         */
        if (empty()) {
            return null;
        } else {
            T currentHead = head.getData();
            // head.getNext().setPrev(null);
            head = head.getNext();
            if (head != null) {
                head.setPrev(null);
            } else { // else if head=null, menaing only one item in que to begin with
                tail = null;
            }
            size--;
            return currentHead;
        }
    }

    public static void main(String[] args) {
        /**
         * main method to test if queue is working
         */
        MyQueue<Integer> test = new MyQueue<>();
        System.out.println(test.size());
        test.offer(37);
        test.offer(2);
        test.offer(1);
        test.offer(100);
        System.out.println("peeking at the head " + test.peek());
        System.out.println("size: " + test.size());
        System.out.println("Print out content");
        Iterator it = test.iterator();
        while (it.hasNext()) {
            int obj = (int) it.next();
            System.out.println(obj);
        }
        test.poll();
        System.out.println("testing " + test.head.getData());
        System.out.println(test.size());
        Iterator second = test.iterator();

        while (second.hasNext()) {
            int obj = (int) second.next();
            System.out.println(obj);
        }
        System.out.println("this should be 1 " + test.tail.getPrev().getData());
        test.clear();
        System.out.println("should be 0 " + test.size());

    }

}