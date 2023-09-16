# Stack
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item): 
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)

# Example usage:
if __name__ == "__main__":
    stack = Stack()

    print("Is the stack empty?", stack.is_empty())

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Stack size:", stack.size())
    print("Top element:", stack.peek())

    while not stack.is_empty():
        print("Popped:", stack.pop())

    print("Is the stack empty?", stack.is_empty())
