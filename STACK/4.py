# Implement Stack using Linked List
class MyStack:  
    class StackNode:
        # Constructor to initialize a node
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    # Function to push an integer into the stack.
    def push(self, data):
        new_node = self.StackNode(data)
        new_node.next = self.head
        self.head = new_node

    # Function to remove an item from the top of the stack.
    def pop(self):
        if not self.head:
            return -1  # Stack is empty, return -1 as per the problem statement.
        popped_data = self.head.data
        self.head = self.head.next
        return popped_data

# Example usage:
stack = MyStack()
stack.push(2)
stack.push(3)
print(stack.pop())  # Output: 3
stack.push(4)
print(stack.pop())  # Output: 4
