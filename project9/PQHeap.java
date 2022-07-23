/**
 * Harsha Somaya
 * 04/19/2022
 * Section Lab C/D
 * Project 9
 * CS 231
 * PQHeap.java
 */
import java.util.ArrayList;
import java.util.Comparator;

public class PQHeap<T> {
    private int size;
    private Comparator<T> comparator;
    private T[] heap;

    public PQHeap(Comparator<T> comparator) {
        /**
         * a constructor that initializes the empty heap, sets the size to zero, and
         * stores the comparator.
         */
        heap = (T[]) new Object[50];
        size = 0;
        this.comparator = comparator;

    }

    public int size() {
        /**
         * returns the number of elements in the heap.
         */
        return size;
    }

    public void add(T obj) {
        /**
         *   // Put this object into the next open slot
        // while this object is sitting at a place that the parent is smaller than it:swap with its parent
         */
        int openSpotIndex = size(); // open index
        if (openSpotIndex==heap.length){  //it is at capacity, expand 
            T[] newHeap= (T[]) new Object[heap.length*2];
            for (int i=0;i<size();i++){ //only for the filled ones, size
                newHeap[i]=heap[i];
            }
            heap=newHeap;
        }
        
        heap[openSpotIndex] = obj;
        size++;
        while (openSpotIndex > 0) {
            T parentData = heap[parent(openSpotIndex)]; //returns the last item before i added object 
            if (comparator.compare(parentData, obj) < 0) { // oject is greater, switch
                heap[parent(openSpotIndex)] = obj;
                heap[openSpotIndex] = parentData;
            }
            openSpotIndex = parent(openSpotIndex);
        }
    }



    public T remove() {
        /**
         * removes and returns the highest priority element from the heap. //give highest
         * or root
         */
        if (size()==0){
            return null;
        }
        T root = heap[0];
        heap[0] = heap[size - 1]; // root replaced with last child   //heap[0]=heap[0]
        heap[size - 1] = null;   //heap[0]=null  last child is null
        int currentIndex = 0;
        size--;
        while (currentIndex < size()) {
            System.out.println("current index "+currentIndex);

            if (heap[leftChild(currentIndex)] == null) {// if left is null, done, meaning only one node
                return root;
            }
           
            else if (heap[rightChild(currentIndex)] == null) {  
                 // if left is not null but right is, then check to see if you need to swap, and
                // then swap if necessary, otherwise done
                if (comparator.compare(heap[currentIndex], heap[leftChild(currentIndex)]) < 0) { // parent is less than left child                                                                             
                    T parentData = heap[currentIndex];
                    heap[currentIndex] = heap[leftChild(currentIndex)];  //parennt ecomes child
                    heap[leftChild(currentIndex)] = parentData;    //left child ecomes what parent was
                    currentIndex=leftChild(currentIndex);  
                }
                else{return root;}   
            }

            else {
                // else (if left and right are not null), figure out which child is bigger, and
                // swap if that child is bigger than me, otherwise done
                T biggerChildData = heap[leftChild(currentIndex)]; // assume is
                T parentData = heap[currentIndex]; // starts off at 0
                if ((comparator.compare(heap[rightChild(currentIndex)], heap[leftChild(currentIndex)]) < 0)) {
                    // left   is bigger than right                                                                                                                                                                                  // bigger
                    biggerChildData = heap[leftChild(currentIndex)];
                    if (comparator.compare(parentData, biggerChildData) < 0) { // parent is less than child , switch
                        heap[currentIndex] = biggerChildData;
                        heap[leftChild(currentIndex)] = parentData;
                        currentIndex=leftChild(currentIndex);  //again

                    }
                    else{return root;}
                }

                else { //right is bigger                                                                                             
                    biggerChildData = heap[rightChild(currentIndex)];
                    if (comparator.compare(parentData, biggerChildData) < 0) { // parent is less, switch
                        heap[currentIndex] = biggerChildData;
                        heap[rightChild(currentIndex)] = parentData;
                        currentIndex=rightChild(currentIndex);
                    }
                    else{return root;}
                }
            }
        }
    
    return root;        
    }

    public T get(int index){
        /**
         * retunrs T at this index 
         */
        return heap[index];
    }

    private int parent(int childIndex) {
        /**
         * retunr parent of given chid index
         */
        return (childIndex - 1) / 2;

    }

    private int leftChild(int parentIndex) {
        /**
         * return left child index given parent child
         */
        return 2 * parentIndex + 1;
    }

    private int rightChild(int parentIndex) {
        /**
         * return left child index given parent child
         */
        return 2 * parentIndex + 2;
    }

    public String toString(){  //has to be pulci to overwrite
        /**
         * visulaize heap as a to string accoridng to the levels
        */ 
        String string="";
        ArrayList<Integer> newLineIndexci = new ArrayList<Integer>();
        newLineIndexci.add(0);   

        for (int i=0; i<Math.log(size())/Math.log(2);i++){
            newLineIndexci.add(newLineIndexci.get(i)*2+2);
        }
        // int nextLineIndex=0;
        for (int i=0; i<size();i++){
            string+=heap[i];
            // if (i==nextLineIndex){
            //     string+="\n";
            //     nextLineIndex=nextLineIndex*2+2;
            // }
            if (newLineIndexci.contains(i)){

                string+="\n";
            }
        }
        return string;
    }
}
