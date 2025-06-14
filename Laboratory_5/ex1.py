# Write a Python class that simulates a Stack.
# The class should implement methods like push, pop, peek (the last two methods should return None if no element is present in the stack).

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return None
        item = self.items[-1]
        self.items.remove(self.items[-1])
        return item

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack.pop())
    print(stack.peek())
    print(stack.is_empty())
    print(stack.size())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.is_empty())
    print(stack.size())
    print(stack.peek())