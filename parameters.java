import java.util.*; 

public class Parameters {
    public List<Integer> itemWeights;
    public List<Integer> itemValues;
    public Integer maxWeightCapacity;
    
    public Parameters(List<Integer> itemWeights, List<Integer> itemValues, Integer maxWeightCapacity) {
        this.itemWeights = itemWeights;
        this.itemValues = itemValues;
        this.maxWeightCapacity = maxWeightCapacity;
    }
    
    public static Parameters easy() {
        var values = new ArrayList<Integer>(){{
            add(9818);
            add(4040);
            add(9560);
            add(9436);
            add(8080);
            add(793);
            add(886);
            add(4294);
            add(474);
            add(2929);
        }};
        
        var weights = new ArrayList<Integer>(){{
            add(7250);
            add(421);
            add(7195);
            add(49);
            add(5077);
            add(1537);
            add(2229);
            add(5653);
            add(2366);
            add(6881);
        }};
        return new Parameters(weights, values, 5);
    }
    
	public static void main(String[] args) {
		System.out.println(easy().itemWeights);
	}
}
