"""Example 1: Find Top Earners"""

# Data
employees = {'Alice': 100000,
             'Bob': 99817,
             'Carol': 122908,
             'Frank': 88123,
             'Eve': 93121}

# One-liner
top_earners = [(k,v) for k, v in employees.items() if v >= 100000]

# Result
print(top_earners)

"""Example 2: Find Words with High Information Value"""

# Data
text = '''Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and n0thing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''

# One-liner
w = [[x for x in line.split() if len(x)>3] for line in text.split('\n')]

# Result
print(w)