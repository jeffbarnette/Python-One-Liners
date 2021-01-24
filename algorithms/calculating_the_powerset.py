"""Example of Calculating the Powerset by using Functional Programming"""

# Dependencies
from functools import reduce

# Data
s = {1, 2, 3}

# One-Liner
ps = lambda s: reduce(lambda P, x: P + [subset | {x} for subset in P], s, [set()])

# Result
print(ps(s))