# The last-in, first-out (LIFO) method.
# Time Complexities: O(1) time.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        if data not in self.stack:
            self.stack.append(data)

    def pop(self):
        if self.stack:
            self.stack.pop()
        else:
            return "No elements in the Stack"

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek())
print(s.size())
s.pop()
print(s.stack)
