"""Example of Finding Prime Numbers using the Sieve of Eratosthenes"""

# Dependencies
from functools import reduce

# Data
n = 100

# One-Liner
primes = reduce(lambda r, x: r - set(range(x**2, n, x)) if x in r else r, \
    range(2, int(n**0.5) + 1), set(range(2, n)))

# Result
print(primes)