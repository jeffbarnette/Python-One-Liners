"""Example of slice assignments to remove and replace corrupted entries"""

# Data
visitors = ['Firefox', 'corrupted', 'Chrome', 'corrupted',
            'Safari', ' corrupted', 'Safari', 'corrupted',
            'Chrome', 'corrupted', 'Firefox', 'corrupted']

# One-liner
visitors[1::2] = visitors[::2]

# Result
print(visitors)