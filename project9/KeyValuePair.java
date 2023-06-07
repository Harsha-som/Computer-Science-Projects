/**
 * Harsha Somaya
 * 04/05/2022
 * Section Lab C/D
 * Project 9
 * CS 231
 * KeyValuePair.java
 */
public class KeyValuePair<Key, Value> {

    private Key key;
    private Value value;

    public KeyValuePair( Key k, Value v ){
        /**
         * constructor initializing the key and value fields.
         */
        key=k;
        value=v;
    }

    public Key getKey(){
        /**
         * returns the key
         */
        return key;
    }

    public Value getValue(){
        /**
         *  returns the value
         */
        return value;
    }

    public void setValue( Value v ){
        /**
         * sets the value.
         */
        value=v;
    }

    public String toString(){
        /**
         * returns a String containing both the key and value.
         */
        return "key:'"+key+"'value: "+value+" ";
    }
        
    public static void main(String[] args) {
        /**
         * main method for testing
         */
        KeyValuePair<Integer,String> test=new KeyValuePair<Integer,String>(4, "value");
        System.out.println(test.getKey());
        System.out.println(test.getValue()); 
        test.setValue("new value");  
        System.out.println(test);
   
    }
    
}