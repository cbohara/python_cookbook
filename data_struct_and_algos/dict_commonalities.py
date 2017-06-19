#!/usr/local/bin/python3

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# keys() returns a keys-view object that supports common set operations
# find keys in common
print(a.keys() & b.keys())

# find keys in a that are not in b
print(a.keys() - b.keys())

# items() returns (key, value) pairs and also supports set operations
# find (key,value) pairs in common
print(a.items() & b.items())

# make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(c)

# values() does not support set operations because values in a dictionary do not need to be unique
# to perform calculations on the value, you need to convert the value into a set
