#!/usr/local/bin/python3

# want to drop the first and last test scores, and use the remaining for the avg?
def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle)/len(middle)

drop_first_last(list(range(0,10)))


# user record contains name, email, and arbitrary number of phone numbers
record = ('Dave', 'dave@email.com', '123-456-7890', '098-765-4321', '123-123-1234')
name, email, *phone_numbers = record
# *variable will always be a list
print(phone_numbers)


# iterate over a sequence of tuples of varying length
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


# use with string splitting
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(fields)
print(homedir)


# clever recursive algorithm
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head
