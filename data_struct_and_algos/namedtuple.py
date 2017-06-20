#!/usr/local/bin/python3
from collections import namedtuple

# typically you access list or tuple elements by position

# sometimes it can be helpful to access elements by name
# collections.namedtuple() is a lot like a normal class instance
Subscriber = namedtuple('Subscriber', ['email', 'joined'])
sub1 = Subscriber('jones@example.com', '2012-10-19')
# Subscriber(email='jones@example.com', joined='2012-10-19')
print(sub1.email)
print(sub1.joined)

# but it supports all the usual tuple operations
print(len(sub1))

# like variable unpacking
email, joined = sub1
print(email)
print(joined)

# major usecase - not having code dependent on position
# ex: you get a large list of tuples froma a database call
# if you add a new column to your table, your code can break if all the logic is positional
# this can be avoided by first transforming the tuples returned from DB to namedtuples

# this code can easily be broken
def compute_cost(records):
    total = 0.0
    for record in records:
        # reference to positional elements often makes code less expressive and more dependent on structure
        total += record[1] * record[2]
    return total

# demo of using namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price'])

def compute_cost(records):
    total = 0.0
    for record in records:
        s = Stock(*record)
        total += s.shares * s.price
    return total

# one possible use of a namedtuple is to replace dictionaries
# pros and cons
# dictionaries take up more memory, but are mutable
# namedtuple takes up less memory, but is immutable 
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
s = Stock('ACME', 100, 123.45)
# cannot assign because tuples are immutable
# s.shares = 75 
# AttributeError: can't set attribute

# if you need to change attribute, use _replace() method
# will make an entirely new namedtuple with the specific value replaced
s = s._replace(shares=75)
print(s)
# Stock(name='ACME', shares=75, price=123.45)

# a creative use of _replace() is to populate namedtuples that have optional or missing fields
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)

# function to convert dictionary to a namedtuple
def dict_to_namedtuple(s):
    return stock_prototype._replace(**s)

a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_namedtuple(a))
# Stock(name='ACME', shares=100, price=123.45, date=None, time=None)

b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_namedtuple(b))
# Stock(name='ACME', shares=100, price=123.45, date='12/17/2012', time=None)
