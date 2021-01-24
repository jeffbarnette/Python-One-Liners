"""Example of working with NumPy Arrays: Slicing, 
Broadcasting, and Array Types"""

# Dependencies
import numpy as np

# Data: Yearly salary in thousands of $ for [2025, 2026, 2027]
dataScientist =     [130, 132, 137]
productManager =    [127, 140, 145]
designer =          [118, 118, 127]
softwareEngineer =  [129, 131, 137]

employees = np.array([dataScientist,
                     productManager,
                     designer,
                     softwareEngineer])

# One-liner
employees[0,::2] = employees[0,::2] * 1.1

# Result
print(employees)