from python_input.from_api import get_data
from dataclasses import dataclass
import random
import timeit

from data import easy, medium, hard


def generate_random_tuple_list():
    return [(random.uniform(1, 100), random.uniform(1, 100)) for i in range(1000)]


def solve_recursive(items: list[tuple[float, float]], maxWeight: float):
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
    
    maxValue = knapSack(maxWeight, list(map(lambda item: float(item[0]), items)), list(map(lambda item: float(item[1]), items)), len(items), res)
    return res, maxValue


def solve_greedy(items: list[tuple[float, float]], maxWeight):

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
        if (totalWeight + weight) <= maxWeight:
            totalWeight += weight
            totalValue += value
            res += [idx]

    return res, totalValue, totalWeight

def solve_greedy_mutate(items: list[tuple[float, float]], maxWeight, mutationRate=0.2):

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
        if (totalWeight + weight) <= maxWeight:
            totalWeight += weight
            totalValue += value
            res += [idx]

    return res, totalValue, totalWeight


def solve_greedy_mutate_bruteforce(items: list[tuple[float, float]], maxWeight):

    bestValue = 0
    bestCombination = []
    bestWeight = 0
    for i in range(10000):
        res, totalValue, totalWeight = solve_greedy_mutate(items, maxWeight)
        if totalValue > bestValue:
            bestValue = totalValue
            bestCombination = res
            bestWeight = totalWeight
    return bestCombination, bestValue, bestWeight



#print(solve_recursive(data3, 100))
#print(solve_greedy(data3, 100))
#print(solve_greedy_mutate_bruteforce(data3, 100))


