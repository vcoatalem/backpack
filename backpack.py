from python_input.from_api import get_data
from dataclasses import dataclass
import random

#data = get_data()

"""
import random

lst = [(random.uniform(1, 100), random.uniform(1, 100)) for i in range(100)]
print(lst)
"""

data = [
    (1, 1),
    (2, 3),
    (3, 2),
    (0.5, 1),
    (5, 2),
    (1, 5)
]

data2 = [(34.76403439025063, 75.06715039438973), (63.864410722181624, 51.827216427343046), (26.75086819528454, 71.54462843538134), (58.77380003221162, 6.568256160417056), (73.47736317927752, 82.38468326473114), (95.77599052803201, 59.286715332952596), (15.299481719706701, 58.568438146603924), (5.847739032460653, 30.73053431865569), (43.5536435721032, 7.654128616759938), (44.56701819612133, 16.36296638352028), (53.38224529049062, 7.739390660163492), (48.795782978105755, 90.64096885693654), (21.40469287260959, 10.191779375987885), (21.84771011425227, 21.2627063021767), (62.382621093101854, 23.744989198898853), (55.48669531504454, 69.27750462425831), (76.14157918936141, 13.199799380029242), (33.59895695107731, 68.86746211170892), (39.48394910001719, 71.65733965623298), (39.82379780954466, 1.68815779273262), (42.975222255792374, 90.14365611516608), (44.559570759221124, 78.54190145926545), (19.86105568116645, 15.222810529386141), (41.94969098129971, 8.920275394428838), (80.12262327478724, 61.23461063911019), (40.355346678815096, 44.67627152295083), (35.37717429450901, 5.9489584329719705), (87.09744671033428, 11.393766268884853), (18.560328839744102, 26.90035748028236), (2.505129708478017, 71.67153793871047), (15.309600626424437, 91.79953296983732), (13.735433701074497, 66.7522286300502), (20.016819502816563, 19.854608287818785), (99.74266189954031, 6.685774673236298), (21.235796223787382, 12.328592511914476), (28.850290968443577, 98.8045514776365), (17.351507277498794, 46.10981141302013), (74.28345960002133, 87.77274287493563), (44.85005165259844, 34.11717057428757), (49.32298631047267, 49.40614501527401), (76.0806385609761, 59.7843385960285), (10.573307715316304, 99.71372437375102), (89.17898405540595, 28.133905819369126), (52.868410366130256, 40.464335655371976), (59.83359095617831, 41.74184182045752), (77.10369502393283, 49.25477448844662), (63.59846260564691, 39.05492810503683), (69.26526271463612, 32.969672482351754), (94.39975742774371, 33.90624072440173), (57.126243723047025, 12.605278408807123), (76.52091399004776, 24.959983202804903), (29.470505174058264, 9.67877972636327), (38.75884615945053, 28.62731904804658), (14.606127359056925, 67.7738223516224), (52.34405728572293, 1.0293124424647426), (70.27383305492245, 64.71382135632902), (16.733971302024027, 99.94610394710567), (20.596867471228567, 16.30217566993187), (92.01196100534857, 57.68767147352224), (16.928274575987928, 79.90327975981694), (26.971554949960073, 43.186190367378515), (53.724837173802364, 80.04790844729511), (42.60704833409728, 84.20475616922437), (42.530170393182935, 35.5775156733317), (4.430551721057657, 25.821309028442187), (37.6933134729919, 21.194578393610627), (49.76189216756763, 27.946648118645697), (53.72451472569224, 55.49387700259409), (56.28452635307925, 60.14700316604595), (55.31750612772455, 71.19461809760774), (60.21569823811067, 39.67609507774163), (13.792328698178297, 45.18627799566527), (81.61481009687176, 23.575839610212228), (29.282410605462996, 72.84167515837159), (38.2425223751625, 84.20087392304028), (62.61707198128094, 95.1700680406621), (19.646902999228995, 34.48163683380943), (55.54080084885962, 17.728538681726874), (99.10564087502186, 43.687929626574615), (89.67552155828507, 91.06445139246051), (83.36966843600956, 97.44706854881018), (56.31880068943541, 46.70457125262138), (36.44286764348986, 77.02683806352005), (16.67417141353293, 20.340430480857425), (12.832324320814594, 44.92325947217523), (50.66018993858193, 35.18069947849861), (91.08120236890889, 99.99352870296954), (91.27221310132738, 36.9444386771731), (59.803975426247476, 89.40513936255219), (11.824531270450073, 59.06239793695341), (58.00780847380487, 67.50730968227556), (91.7705393704274, 40.44098203534398), (66.54365022087796, 34.46815341964341), (62.1534547676853, 9.985408932270353), (85.165127433743, 59.59313475474441), (69.04228450664611, 17.203613212207053), (5.814142841001889, 27.40745167945558), (48.08170977251549, 56.903363293887914), (35.12364397113935, 84.05783257287791), (4.855302371288175, 51.2925061412588)]

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
    return bestCombination, bestValue, maxWeight

print(random.uniform(1, 100), (0.2 * 100))

print(solve_recursive(data2, 100))
print(solve_greedy(data2, 100))
print(solve_greedy_mutate_bruteforce(data2, 100))