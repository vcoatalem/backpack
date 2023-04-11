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
    bestCombination.sort()
    return bestCombination, bestValue, bestWeight

# https://www.askpython.com/python/examples/knapsack-problem-dynamic-programming
def solve_dynamic(params: Parameters):#(W, wt, val):
    W, wt, val = params.maxWeightCapacity, params.itemWeights, params.itemValues
    n = len(val)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]
    selected_items = [[False for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif wt[i-1] <= j:
                table[i][j] = max(val[i-1] + table[i-1][j-wt[i-1]], table[i-1][j])
                if val[i-1] + table[i-1][j-wt[i-1]] > table[i-1][j]:
                    selected_items[i][j] = True
            else:
                table[i][j] = table[i-1][j]

    weight_selected = 0
    indices_selected = []
    j = W
    for i in range(n, 0, -1):
        if selected_items[i][j]:
            weight_selected += wt[i-1]
            indices_selected.append(i-1)
            j -= wt[i-1]

    indices_selected.sort()
    return table[n][W], weight_selected, indices_selected


#val = [50,100,150,200]
#wt = [8,16,32,40]
#W = 64
 


params = Parameters.easy()
#print(solve_greedy(params))
print(solve_greedy_mutate_bruteforce(params))
#print(solve_dynamic(params))
print(solve_dynamic(params))

# easy:
# 28772
# 19092
# [0, 1, 3, 4, 5, 6, 8]


# medium:
# 200475
# 59392
# [0, 7, 10, 11, 12, 14, 31, 36, 37, 38, 41, 45, 49, 51, 53, 54, 56, 58, 60, 62, 63, 65, 67, 68, 72, 73, 75, 85, 87, 96, 97]

# hard:
# 847430
# 119999
# [4, 5, 8, 13, 27, 34, 35, 37, 42, 48, 50, 65, 72, 73, 74, 87, 94, 98, 124, 134, 138, 143, 147, 155, 186, 195, 204, 208, 212, 217, 221, 222, 245, 250, 258, 261, 267, 273, 275, 282, 294, 298, 309, 311, 315, 317, 336, 349, 365, 369, 370, 374, 375, 410, 413, 415, 420, 423, 428, 429, 431, 436, 450, 455, 456, 465, 466, 481, 483, 487, 493, 508, 514, 517, 527, 547, 560, 565, 569, 573, 589, 594, 601, 605, 621, 623, 632, 647, 653, 660, 673, 688, 728, 731, 743, 744, 758, 765, 768, 786, 790, 800, 803, 838, 843, 865, 886, 898, 908, 946, 947, 948, 951, 968, 970, 972, 982, 985, 998]