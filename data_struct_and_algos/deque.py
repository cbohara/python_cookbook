#!/usr/local/bin/python3
from collections import deque

# perform simple text match and yield matching line along with previous N lines
def search(lines, pattern, history=5):
    # create a fixed len queue
    # if a new item is added and the queue is full, the oldest item is automatically removed
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            # instead of using return for a single value
            # use yield to return an iterator object = an object you can iterate over using next
            yield line, previous_lines
        previous_lines.append(line)

# example use on a file
if __name__ == "__main__":
    with open('test.txt') as f:
        # search() will create generator object that can be iterated over
        # however the code is not run all at once
        # only calls to next will execute the next step of the code
        # next is taken care of by the for loop
        for line, prevlines in search(f, 'python', 2):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)

############################################################################################
# in general you can use deque to get an unbounded queue that you can be append at either end
q = deque()
q.append(1)
q.append(2)
q.append(3)
# deque([1, 2, 3])
q.appendleft(1)
# deque([1, 1, 2, 3])
q.pop()
# deque([1, 1, 2])
p.popleft()
# deque([1, 2])
