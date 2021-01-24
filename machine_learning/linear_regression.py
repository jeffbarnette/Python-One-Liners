"""Example of Linear Regression"""

# Dependencies
from sklearn.linear_model import LinearRegression
import numpy as np

# Data (Apple stock prices over 5 days)
apple = np.array([155, 156, 157, 156, 157])
n = len(apple)

# One-liner
model = LinearRegression().fit(np.arange(n).reshape((n,1)), apple)

# Result & prediction for days 6 to 10
print(model.predict([[6], [7], [8], [9], [10]]))