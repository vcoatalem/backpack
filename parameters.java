import java.util.*; 
/*
Online Java - IDE, Code Editor, Compiler

Online Java is a quick and easy tool that helps you to build, compile, test your programs online.
*/


public class Parameters {
    public List<Float> itemWeights;
    public List<Float> itemValues;
    public Float maxWeightCapacity;
    
    public Parameters(List<Float> itemWeights, List<Float> itemValues, Float maxWeightCapacity) {
        this.itemWeights = itemWeights;
        this.itemValues = itemValues;
        this.maxWeightCapacity = maxWeightCapacity;
    }
    
    public static Parameters easy() {
        var weights = new ArrayList<Float>(){{
         add(1.2f);
         add(2.7f);
        }};
        
        var values = new ArrayList<Float>(){{
         add(4.7f);
         add(3.7f);
        }};
        return new Parameters(weights, values, 5f);
    }
    
	public static void main(String[] args) {
		System.out.println(easy().itemWeights);
	}
}
