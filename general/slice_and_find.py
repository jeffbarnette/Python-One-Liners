""" Example of Slicing and Finding"""

# Data
letters_amazon = '''We sepent several years building our own database engine,
Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatiable
service with the same or better durability and availability as
the commerical engines, but at one-tenth of the cost. We were
not surprised when this worked.'''

# One-liner
find = lambda x, q: x[x.find(q)-18:x.find(q)+18] if q in x else -1

# Result
print(find(letters_amazon, 'SQL'))