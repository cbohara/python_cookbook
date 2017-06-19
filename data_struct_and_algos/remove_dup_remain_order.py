#!/usr/local/bin/python3

# use set() to eliminate duplicates
# however set() will not preserve original ordering
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(set(a))
# {1, 2, 5, 9, 10}

# you want to eliminate duplicate values in a sequence, but preserve the order of the remaining items
# if the values are hashable, the problem can be solved using a set and a generator 
def no_duplicates(items):
    # hash values are used to ID unique values
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

# list values are hashable 
# a hash is a fixed sized integer that IDs a particular value
# hash("Look at me") = 4343814758193556824
# f = "Look at me"
# hash(f) = 4343814758193556824

# hash(1) = 1
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(no_duplicates(a)))

# very cool use case = read a file and eliminate duplicate lines
with open('no_repeat.txt', 'w') as out_f:
    with open('example.txt', 'r') as in_f:
        for line in no_duplicates(in_f):
            out_f.write(line)
