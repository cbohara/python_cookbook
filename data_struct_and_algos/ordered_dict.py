#!/usr/local/bin/python3
from collections import OrderedDict

# interally = doubly linked list that orders keys by insertion order
# be aware that OrderedDict takes up 2x the memory vs normal dict 
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

# preserves the original insertion order of data when iterating
for key, value in d.items():
    print(key, value)
