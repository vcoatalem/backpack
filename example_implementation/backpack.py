from parameters import Parameters
from dataclasses import dataclass
import random
import timeit


def generate_random_tuple_list():
    return [(random.uniform(1, 100), random.uniform(1, 100)) for i in range(1000)]


def solve_recursive(params: Parameters):
    res = []
    # https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
    def knapSack(W, wt, val, n, selected: list[int]):
        # Base Case: went through all items, or bag is full
        if n == 0 or W == 0:
            return 0
    
        # If weight of the nth item is
        # more than Knapsack of capacity W,
        # then this item cannot be included
        # in the optimal solution
        if wt[n - 1] > W:
            return knapSack(W, wt, val, n - 1, selected)
    
        # return the maximum of two cases:
        # (1) nth item included
        # (2) not included
        else:
            tryIncludeArray = selected[:] + [n - 1]
            tryExcludeArray = selected[:]
            tryInclude = val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1, tryIncludeArray)
            tryExclude = knapSack(W, wt, val, n - 1, tryExcludeArray)
            if (tryInclude > tryExclude):
                selected[:] = tryIncludeArray
            else:
                selected[:] = tryExcludeArray
            return max(tryInclude, tryExclude)
    
    maxValue = knapSack(params.maxWeightCapacity, params.itemWeights, params.itemValues, len(params.itemValues), res)
    return res, maxValue


#def solve_greedy(items: list[tuple[float, float]], maxWeight):
def solve_greedy(params: Parameters):

    items = [(params.itemWeights[i], params.itemValues[i]) for i in range(len(params.itemValues))]

    def heuristic(item: tuple[float, float]) -> float:
        weight = item[0]
        value = item[1]
        return value / weight

    weightedIndexes: list[tuple[int, float]] = [(i, heuristic(x), x[0], x[1]) for i,x in enumerate(items)]
    weightedIndexes.sort(key=lambda elt: elt[1], reverse=True)

    #print(weightedIndexes)

    res = []
    totalValue = 0.0
    totalWeight = 0.0
    for (idx, ratio, weight, value) in weightedIndexes:
        if (totalWeight + weight) <= params.maxWeightCapacity:
            totalWeight += weight
            totalValue += value
            res += [idx]

    return res, totalValue, totalWeight

def solve_greedy_mutate(params: Parameters, mutationRate=0.2):

    items = [(params.itemWeights[i], params.itemValues[i]) for i in range(len(params.itemValues))]

    def heuristic(item: tuple[float, float]) -> float:
        weight = item[0]
        value = item[1]
        return value / weight

    weightedIndexes: list[tuple[int, float]] = [(i, heuristic(x), x[0], x[1]) for i,x in enumerate(items)]
    weightedIndexes.sort(key=lambda elt: elt[1], reverse=True)

    #print(weightedIndexes)

    res = []
    totalValue = 0.0
    totalWeight = 0.0
    for (idx, ratio, weight, value) in weightedIndexes:
        if random.uniform(1, 100) < mutationRate * 100:
            continue
        if (totalWeight + weight) <= params.maxWeightCapacity:
            totalWeight += weight
            totalValue += value
            res += [idx]

    return res, totalValue, totalWeight

def solve_greedy_mutate_bruteforce(params: Parameters, nTries=10000):
    bestValue = 0
    bestCombination = []
    bestWeight = 0
    for i in range(nTries):
        res, totalValue, totalWeight = solve_greedy_mutate(params)
        if totalValue > bestValue:
            bestValue = totalValue
            bestCombination = res
            bestWeight = totalWeight
    return bestCombination, bestValue, bestWeight


params = Parameters.hard()
#print(solve_recursive(params))
print(solve_greedy(params))
print(solve_greedy_mutate(params))
print(solve_greedy_mutate_bruteforce(params, 10000))

#print(solve_recursive(data3, 100))
#print(solve_greedy(data3, 100))
#print(solve_greedy_mutate_bruteforce(data3, 100))


# easy:
# ([1, 8, 4, 0, 3, 5, 6], 28772.0, 19092.0)


# medium:
# ([7, 62, 65, 12, 68, 63, 56, 85, 58, 37, 75, 11, 10, 60, 87, 72, 0, 54, 45, 53, 51, 73, 67, 41, 14, 97, 36, 49, 38, 96, 31], 200475.0, 59392.0)
