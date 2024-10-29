# Write a Python class that simulates a Queue.
# The class should implement methods like push, pop, peek (the last two methods should return None if no element is present in the queue).

class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop(0)

    def peek(self):
        if not self.items:
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print(queue.pop())
    print(queue.peek())
    print(queue.is_empty())
    print(queue.size())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.is_empty())
    print(queue.size())
    print(queue.peek())