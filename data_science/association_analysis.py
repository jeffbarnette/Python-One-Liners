"""Example of simple association analysis: 
People who bought X also bought Y"""

# Dependencies
import numpy as np

# Data: row is customer shoppoing basket
# row = [course 1, course 2, ebook 1, ebook 2]
# value 1 indicates that an item was bought.
basket = np.array([[0, 1, 1, 0],
                  [0, 0, 0, 1],
                  [1, 1, 0, 0],
                  [0, 1, 1, 1],
                  [1, 1, 1, 0],
                  [0, 1, 1, 0],
                  [1, 1, 0, 1],
                  [1, 1, 1, 1]])

# One-liner
copurchases = np.sum(np.all(basket[:,2:], axis = 1)) / basket.shape[0]

# Result
print(copurchases)