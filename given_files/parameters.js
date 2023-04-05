class Parameters {
    constructor(itemWeights, itemValues, maxWeightCapacity) {
        this.itemWeights = itemWeights;
        this.itemValues = itemValues;
        this.maxWeightCapacity = maxWeightCapacity;
    }

    static easy() {
        const values = [7250, 421, 7195, 49, 5077, 1537, 2229, 5653, 2366, 6881];
        const weights = [9818, 4040, 9560, 9436, 8080, 793, 886, 4294, 474, 2929];
        return new Parameters(weights, values, 5);
    }
}

console.log(Parameters.easy())