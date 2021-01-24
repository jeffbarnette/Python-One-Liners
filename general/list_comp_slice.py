"""Example of creating new training data from a larger data set"""

# Data (Daily stock prices in $)
price = [[9.9, 9.8, 9.8, 9.4, 9.5, 9.7],
          [9.5, 9.4, 9.4, 9.3, 9.2, 9.1],
          [8.4, 7.9, 7.9, 8.1, 8.0, 8.0],
          [7.1, 5.9, 4.8, 4.8, 4.7, 3.9]]

# One-liner
sample = [line[::2] for line in price]

# Result
print(sample)