#!/usr/local/bin/python3
# heaps are binary trees - each parent node has a value less than or equal to any of its children
import heapq

# BETTER TO USE SORTED() if you want to get the min or max elements from a list
# this is more theoretical vs practical
# you want to make a list of the largest and smallest N items in a collection
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

# both functions also take key parameter = can use on more complicated data structures
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
]

cheap = heapq.nsmallest(2, portfolio, key=lambda s: s['price'])
print(cheap)
expensive = heapq.nlargest(2, portfolio, key=lambda s: s['price'])
print(expensive)

# underneath the covers nsmallest and nlargest convert data to a list where items are ordered as a heap
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = heapq.heapify(nums)
# [-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]
