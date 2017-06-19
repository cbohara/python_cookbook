#!/usr/local/bin/python3
from operator import itemgetter

# let's say we have queried the database table to get a list of dictionaries that rep each member
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

# use itemgetter to id the key you want to compare in the dictionary
rows_by_fname = sorted(rows, key=itemgetter('fname'))
print('Sorted by first name')
print(rows_by_fname)

rows_by_uid = sorted(rows, key=itemgetter('uid'))
print('Sorted by last name')
print(rows_by_uid)

# can also be used to ID mix and max for ints
print('Min uid')
print(min(rows, key=itemgetter('uid')))
print('Max uid')
print(max(rows, key=itemgetter('uid')))

# can also sort first by last name, and if the last name is the same, sort by first name
rows_by_last_first_name = sorted(rows, key=itemgetter('lname', 'fname'))
print('Sorted by last name, then by first name')
print(rows_by_last_first_name)
