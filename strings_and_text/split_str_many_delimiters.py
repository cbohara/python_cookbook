import re

line = 'asdf fjdk; afed, fjek,asdf, foo'

# re.split is useful for specifying multiple delimiters
# re.split returns a list just like the os.split
# ex: find all instances of ; , and spaces followed by any numbers of spaces
parsed = re.split(r'[;,\s]\s*', line)
print(parsed)
