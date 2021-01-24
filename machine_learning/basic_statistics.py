"""Example of Basic Statistics"""

# Dependencies
import numpy as np

# Data: Stock Prices (5 companies)
# (row=[price_day_1, price_day_2, ...])
x = np.array([[8, 9, 11, 12],
             [1, 2, 2, 1],
             [2, 8, 9, 9],
             [9, 6, 6, 3],
             [3, 3, 3, 3]])

# One-liner
avg, var, std = np.average(x, axis=1), np.var(x, axis=1), np.std(x, axis=1)

# Result & Prediction
print("Averages: " + str(avg))
print("Variances: " + str(var))
print("Standard Deviations: " + str(std))