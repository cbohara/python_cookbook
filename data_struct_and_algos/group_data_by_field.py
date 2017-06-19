#!/usr/local/bin/python3
from operator import itemgetter
from itertools import groupby

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

# sort by date
# sort() modifies the list in place while sorted() returns a new sorted list and keeps the original in tact
# it is necessary to sort() before using groupby()
rows.sort(key=itemgetter('date'))

# iterate in groups
# on each iteration, groupby() will return the value (date)
# along with an iterator that produces all the items in a group with the same value
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print('   ', i)

# method above is helpful when you want to group data without using additional memory resources
# it is slower to have to sort and then groupby though

# if you want to store this sorted data in a data structure and memory is no concern
# better off using defaultdict()
# don't have to sort first = faster
from collections import defaultdict

rows_by_date = defaultdict(list)
for row in rows:
    # date will be a key for rows_by_date with each row appended to list of dict values 
    rows_by_date[row['date']].append(row)

# now we have a data structure that allows random access
for r in rows_by_date['07/01/2012']:
    print(r)
