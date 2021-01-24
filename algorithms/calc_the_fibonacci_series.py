"""Example of Calculating the Fibonacci Series with the reduce() function"""

# Dependencies
from functools import reduce

# Data
n = 10

# One-Liner
fibs = reduce(lambda x, _: x + [x[-2] + x[-1]], [0] * (n-2), [0, 1])

# Result
print(fibs)