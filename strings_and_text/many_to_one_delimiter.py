import re

line = 'asdf fjdk; afed, fjek,asdf, foo'

# if re groups are used using (), then matched text is also included in the result
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)

# from index 0 to the end, grab every other element in the list
values = fields[::2]
# from index 1 to the end, grab every other element in the list
delimiters = fields[1::2] + ['']

# change the input line so uniform space delimiter is used
uniform = ''.join(v+d for v,d in zip(values, delimiters))
print(uniform)
