#!/usr/local/bin/python3

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

high_price = {key:value for key, value in prices.items() if value > 200}
print(high_price)

tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
tech = {key:value for key, value in prices.items() if key in tech_names}
print(tech)
