"""Example of Boolean Indexing of Two-Dimensional Arrays"""

# Dependencies
import numpy as np

# Data: popular Instagram accounts (millions of followers)
inst = np.array([[232, "@instagram"],
                 [133, "@selenagomez"],
                 [59, "@victoriassecret"],
                 [120, "@cristiano"],
                 [111, "@beyonce"],
                 [76, "@nike"]])

# One-liner
superstars = inst[inst[:,0].astype(float) > 100, 1]

# Results
print(superstars)