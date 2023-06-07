/**
 * Harsha Somaya
 * 04/05/2022
 * Section Lab C/D
 * Project 8
 * CS 231
 * MyDoublyLinkedList.java
 */


/**
* MyDoublyLinkedList.java
* Doubly Linked List
* Hannah Wolfe, Oliver W. Layton and Zadia Codabux
* CS231: Data structures and algorithms, Spring 2022
*/

import java.util.Iterator;

public class MyDoublyLinkedList<T> implements Iterable<T> {
	private int size;
	private Node<T> head;
	private Node<T> tail;

	// constructs stack 
	public MyDoublyLinkedList() {
		/**
		 * constructs stack
		 */
		size = 0;
		head = null;
		tail = null;
	}
	
	private class Node <T> {
		private T data;
		private Node<T> next;
		private Node<T> prev;

		public Node(T val, Node<T> next, Node<T> prev) {
			/**
			 * makes a single node
			 */
			data = val;
			this.next = next;
			this.prev = prev;
		}

		public T getData(){
			/**
			 * return teh data at a specific node
			 */
			return data;
		}
		
		public Node<T> getNext() {
			/**
			 * return next node 
			 */
			return next;
		}

		public void setNext( Node<T> n ) {
			/**
			 * set the next to the argument node
			 */
			next = n;
		}

		public Node<T> getPrev() {
			/**
			 * get the previous node
			 */
			return prev;
		}

		public void setPrev( Node<T> n ) {
			/**
			 * set the previous node to a certain argument 
			 */
			prev = n;
		}
	}

	public Iterator<T> iterator() {
		/**
		 * calls the iterare method
		 */
		return new MyLinkedListIterator(head);

	}

	public class MyLinkedListIterator implements Iterator<T> {

		private Node<T> nextNode;

		public MyLinkedListIterator(Node<T> head){
			/**
			 * constructor for iteratr 
			 */
			nextNode = head;
		}

		public T next() {
			/**
			 * give the next node;s data 
			 */
			if (hasNext()){
				T data = nextNode.getData();
				nextNode =nextNode.getNext();
				return data;
			} else {
				return null;
			}
		}

		public boolean hasNext() {
			/**
			 * return true if there is a next node 
			 */
			if (nextNode != null) {
				return true;
			} else {
				return false;
			}
		}

	

	}

	
	public int size(){
		/**
		* Returns the number of elements in the stack. 
		* @return number of elements in the stack
		*/
		return size;
	}

	
	public boolean empty(){
		/**
		* Tests whether the stack is empty.
		* @return true if the stack is empty, false otherwise 
		*/
		if (size() == 0){
			return true;
		} else {
			return false;
		}
	}

	
	public void addFirst(T e) {
		/**
		* Inserts an element at the top of the stack. 
		* @param e the element to be inserted
		*/
		Node<T> newNode = new Node<T>(e, this.head, null);
		if (size ==0) {
			this.tail = newNode;
		}
		this.head = newNode;
		size++;

	}
	


	public T getFirst(){
		/**
		 * return data at head
		 */
		if (!empty()) {
			return head.getData();
		} else {
			return null;
		}
	}

	public T getLast(){
		/**
		 * return dat aat tail
		 */
		if (!empty()) {
			return tail.getData();
		} else {
			return null;
		}
	}

	public T removeFirst(){
		/**
		 * remove the first node's 
		 */
		if (!empty()) {
			T data = head.getData();
			head = head.getNext();
			head.setPrev(null);
			size--;
			return data;
		} else {
			return null;
		}
	}

	public void addLast(T item) {
		/**
		 * add item to the end 
		 */
		Node<T> newNode = new Node<T>(item, null, tail);
		if (!empty()) {
			tail.setNext(newNode);
		} else {
			head = newNode;
		}
		size++;
		tail = newNode;
	}
 	
 
 	public void clear() {
		 /**
		  * clears the linked list 
		  */
		size = 0;
		head = null;
	}

 	public String toString() {
		 /**
		  * viuslaizes the linked list 
		  */
 		Node<T> current = head;
 		String s = "";
 		while(current != null){
 			s += current.getData() + ", ";
 			current = current.getNext();
 		}
 		return s;
 	}


	public static void main(String[] args){
		/**
		 * test the linked list
		 */
		MyDoublyLinkedList<Integer> ll = new MyDoublyLinkedList<Integer>();
		
		System.out.println(ll.size());
		ll.addFirst(37);
		ll.addFirst(2);
		ll.addFirst(1);
		ll.addFirst(100);
		ll.addLast(4);
		System.out.println(ll.getFirst());
		System.out.println(ll.getLast());
		ll.removeFirst();
		System.out.println("size: " + ll.size());
		System.out.println("Print out content");
		Iterator it = ll.iterator();
		while(it.hasNext()) {
      		int obj = (int)it.next();
      		System.out.println(obj);
    	}
		System.out.println(ll.size());
		ll.clear();
		System.out.println(ll.toString());
	}
	
}