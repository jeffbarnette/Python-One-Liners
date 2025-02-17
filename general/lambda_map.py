""" Example of using Lambda and Map Functions"""

# Data
txt = ["lambda functions are anonymous functions.",
       "anonymous functions don't have a name.",
       "functions are objects in Python."]

# One-Liner
mark = map(lambda s: (True, s) if 'anonymous' in s else (False, s), txt)

# Result
print(list(mark))