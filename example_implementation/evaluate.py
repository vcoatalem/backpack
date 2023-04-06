import timeit

from backpack import solve_recursive, solve_greedy, solve_greedy_mutate_bruteforce
from parameters import Parameters

easy = Parameters.easy()
medium = Parameters.medium()
hard = Parameters.hard()

resultEasy = timeit.timeit(stmt='solve_greedy_mutate_bruteforce(easy)', globals=globals(), number=10)
resultMedium = timeit.timeit(stmt='solve_greedy_mutate_bruteforce(medium)', globals=globals(), number=10)
resultHard = timeit.timeit(stmt='solve_greedy_mutate_bruteforce(hard)', globals=globals(), number=10)
print(resultEasy, resultMedium, resultHard)
# 0.6641042230003222 7.372793710999758 82.49624289900021

"""
resultEasy = timeit.timeit(stmt='solve_recursive(easy, easy_max_weight)', globals=globals(), number=10)
resultMedium = timeit.timeit(stmt='solve_recursive(medium, medium_max_weight)', globals=globals(), number=10)
resultHard = timeit.timeit(stmt='solve_recursive(hard, hard_max_weight)', globals=globals(), number=10)
print(resultEasy, resultMedium, resultHard)
"""

# maximum recusrion depth reached