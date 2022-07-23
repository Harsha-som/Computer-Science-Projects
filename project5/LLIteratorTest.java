/**
 * Harsha Somaya
 * 03/18/2022
 * Section Lab C/D
 * Project 5
 * CS 231
 */
/*
	Bruce A. Maxwell
	CS 231 Project 5
	Linked List test function for the Iterator
*/

public class LLIteratorTest {

	public static void main(String[] args) {
		/**
		 * the test of rthe iterator
		 */
		
		LinkedList<Integer> llist = new LinkedList<Integer>();

		// add ten numbers to the list, in order
		for(int i=0;i<5;i++) {
				llist.addFirst(i);
		}
		System.out.println("There are " + llist.size() + " lights");

		llist.clear();

		System.out.println("There are " + llist.size() + " lights");

		for(int i=0;i<4;i++) {
				llist.addFirst(i);
		}

		System.out.println("There are " + llist.size() + " lights");

		// execute a foreach loop
		for(Integer q: llist) {
				System.out.println("value: " + q);
		}
		
	}
}