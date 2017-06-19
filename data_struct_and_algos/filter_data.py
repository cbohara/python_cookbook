#!/usr/local/bin/python3
import math

# list comprehension are most straightforward
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
positives = [x for x in mylist if x > 0]
print(positives)

# filter and transform data
sqrt = [math.sqrt(n) for n in mylist if n > 0]
print(sqrt)

# can also replace values that don't mean criteria with a new value
# replace negative numbers with 0
no_neg = [n if n > 0 else 0 for n in mylist]
print(no_neg)

# potential downside of list comp is that it will produce a large result if input is large
# if this is a concern, use a generator > lazy evaluation = use less memory vs list comp
positives = (n for n in mylist if n > 0)
for x in positives:
    print(x)

# for more complicated filtering, make your own function
values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

# filter() creates an iterator 
ints = list(filter(is_int, values))
print(ints)

###################################################################
from itertools import compress

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK'
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

# counts are associated with the number of instances of each address
counts = [0, 3, 10, 4, 1, 7, 6, 1]
# create a list of booleans
more5 = [n > 5 for n in counts]
print(list(compress(addresses, more5)))

########################################################################
# I think it would make more sense to use a dictionary in this example though
pet_tally = {'dogs': 5, 'cats': 3, 'rabbits': 1, 'turtles': 2}
popular_pets = {key: value for key, value in pet_tally.items() if value > 2}
print(popular_pets)
