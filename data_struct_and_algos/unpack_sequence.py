#!/usr/local/bin/python3
# unpack N-element tuple/sequence into a collection of N variables

# unpacking works for any iterable object
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, (year, month, day) = data
print(name)
print(year)

# convention to use _ for throwaway variables 
_, shares, price, _ = data
