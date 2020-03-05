# A double-ended queue (deque) used to add/remove elements from either end.
# O(1) time complexity for append and pop.

from collections import deque

class Deque:
    def __init__(self):
        self.q = deque()

    def insert_first(self, data):
        if data not in self.q:
            self.q.appendleft(data)

    def insert_last(self, data):
        if data not in self.q:
            self.q.append(data)

    def pop_first(self):
        if self.q:
            self.q.popleft()

    def pop_last(self):
        if self.q:
            self.q.pop()

    def reverse_deque(self):
        return self.q.reverse()

    def size(self):
        return len(self.q)

d = Deque()
d.insert_last(1)
d.insert_first(2)
d.insert_first(3)
d.insert_first(0)
print(d.q)
print(d.size())
d.pop_first()
d.pop_last()
print(d.q)
d.reverse_deque()
print(d.q)