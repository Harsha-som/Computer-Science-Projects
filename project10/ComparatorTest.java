import java.util.Comparator;
public class ComparatorTest implements Comparator <Vertex> {
    public int compare(Vertex o1, Vertex o2){
        return o1.compareTo(o2);
    }
}
