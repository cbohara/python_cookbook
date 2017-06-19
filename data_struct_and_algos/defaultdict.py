#!/usr/local/bin/python3
from collections import defaultdict

# mapping keys to multiple values in a dictionary
# use a list if you want to preserve the insertion order of items
one = {
    'a': [1, 2, 3],
    'b': [4, 5]
}

# use a set when order doesn't matter and you want to eliminate duplicates 
two = {
    'a': {1, 2, 3},
    'b': {4, 5}
}

# can use defaultdict to construct a multidict
# automatically initializes the first value
dd = defaultdict(list)
dd['a'].append(1)
dd['a'].append(2)
dd['a'].append(3)
dd['b'].append(4)
dd['b'].append(5)

# useful for initializing dictionaries
pairs = [('a', 1), ('a', 2), ('a', 3), ('b', 4), ('b', 5)]

# instead of doing....
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

# you can write cleaner code with defaultdict
dd = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
