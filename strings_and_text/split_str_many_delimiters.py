import re

line = 'asdf fjdk; afed, fjek,asdf, foo'

# re.split is useful for specifying multiple delimiters and returns a list
# [;,\s] matches any ; , or space in the text followed by \s* (any number of spaces)
parsed = re.split(r'[;,\s]\s*', line)
print(parsed)
