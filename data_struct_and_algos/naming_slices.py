#!/usr/local/bin/python3

# name slices for readability 
# slice() creates a slice object that can be applied to any object a slice is allowed
items = [2, 4, 6, 8, 1, 3, 5, 7]
evens = slice(0, 4)
print(items[evens])

# equivalent to [4:]
odds = slice(4, None)
print(items[odds])

del items[evens]
print(items)

# you can look at slice object attributes
a = slice(10, 50, 2)
print(a.start)
print(a.stop)
print(a.step)
