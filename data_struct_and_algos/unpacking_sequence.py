#!/usr/local/bin/python3
# Unpack N-element tuple/sequence into a collection of N variables

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, (year, month, day) = data
print(name)
print(year)
