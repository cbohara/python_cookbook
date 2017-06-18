#!/usr/local/bin/python3
import heapq

# implement queue that sorts items by a given priority
# and returns the item with the highest priority on each pop 
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        # heappop will return the smallest item from the heap
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q._queue)
# [(-5, 1, Item('bar')), (-1, 0, Item('foo')), (-4, 2, Item('spam')), (-1, 3, Item('grok'))]

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
