#!/usr/local/bin/python3

# in order to perform useful calculations on dictionary contents, 
# it is often useful to invert keys and values using zip()

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IMB': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# zip makes an iterator that aggregates elements from input iterables
# and returns an iterator of tuples
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

# note - zip creates an iterator that can only be consumed once
prices_and_names = zip(prices.values(), prices.keys())
# this works
print(min(prices_and_names))
# this returns ValueError: max() arg is an empty sequence
print(max(prices_and_names))
