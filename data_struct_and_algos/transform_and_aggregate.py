#!/usr/local/bin/python3

# first need to transform or filter data
# then do some sort of aggregation (ex: sum, min, max)

# a less efficient alternative requires an extra list in memory
nums = [1, 2, 3, 4, 5]
sum_of_squares = sum([x * x for x in nums])

# instead use generator-expression argument
nums = [1, 2, 3, 4, 5]
# do not need an additional pair of parathesis
sum_of_squares = sum(x * x for x in nums)
print(sum_of_squares)

#############################################################################
# determine if any .py files exist in a directory
import os
# listdir() defaults to current directory
files = os.listdir()
# any() returns True if any element in the iterable is true
if any(f.endswith('.py') for f in files):
    print('There be python!')
else:
    print('Sorry no python :(')

#############################################################################
# output a tuple as a csv
stock = ('ACME', 50, 123.45)
# generator expression creates an iterable, transforming data to strings
# str.join(iterable) will return a string that concats strings in iterable
print(','.join(str(x) for x in stock))

#############################################################################
# data reduction across fields of a data structure
portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
]

min_shares = min(s['shares'] for s in portfolio)
print(min_shares)
# 20

# alternative if aggregation function accepts key argument 
min_shares = min(portfolio, key=lambda s: s['shares'])
print(min_shares)
# {'name': 'AOL', 'shares': 20}
