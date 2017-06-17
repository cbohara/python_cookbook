#!/usr/local/bin/python3
# use generator to implement custom iteration pattern
# generator functions will only run in response to an iteration

# produce a range of floating point numbers
def float_range(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

for n in float_range(0, 4, 0.25):
    print(n)

float_list = list(float_range(0, 4, 0.25))

# demonstrate how generators work
def countdown(n):
    print("Starting to countdown from", n)
    while n > 0:
        yield n
        n -= 1
    print("Done!")

# create generator, but notice that no output appears
c = countdown(3)
print(c)
# generator functions only run in response to next function
next(c)
next(c)
next(c)
