import timeit

from data import easy, medium, hard, easy_max_weight, medium_max_weight, hard_max_weight

from backpack import solve_recursive, solve_greedy, solve_greedy_mutate_bruteforce

"""
resultEasy = timeit.timeit(stmt='solve_greedy_mutate_bruteforce(easy, easy_max_weight)', globals=globals(), number=10)
resultMedium = timeit.timeit(stmt='solve_greedy_mutate_bruteforce(medium, medium_max_weight)', globals=globals(), number=10)
resultHard = timeit.timeit(stmt='solve_greedy_mutate_bruteforce(hard, hard_max_weight)', globals=globals(), number=10)
print(resultEasy, resultMedium, resultHard)
"""
# 0.6641042230003222 7.372793710999758 82.49624289900021

"""
resultEasy = timeit.timeit(stmt='solve_recursive(easy, easy_max_weight)', globals=globals(), number=10)
resultMedium = timeit.timeit(stmt='solve_recursive(medium, medium_max_weight)', globals=globals(), number=10)
resultHard = timeit.timeit(stmt='solve_recursive(hard, hard_max_weight)', globals=globals(), number=10)
print(resultEasy, resultMedium, resultHard)
"""

# maximum recusrion depth reached