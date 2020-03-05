# The first-in, first-out (FIFO) method. O(n) time complexity.
# Using the list as a queue not very efficient and slow because
# inserting and deleting requires all elements to shift one by one.

class Queue:
    def __init__(self):
        self.queue = []

    def push(self, data):
        if data not in self.queue:
            self.queue.append(data)

    def pop(self):
        if self.queue:
            self.queue.pop(0)
        else:
            return "No elements in Queue"

    def size(self):
        return len(self.queue)

q = Queue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
print(q.queue)
print(q.size())
q.pop()
print(q.queue)
