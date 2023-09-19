# Implement stack using array  
class MyStack:
    
    def __init__(self):
        self.arr = []
    
    # Function to push an integer into the stack.
    def push(self, data):
        # Append the data to the end of the array.
        self.arr.append(data)
    
    # Function to remove an item from the top of the stack.
    def pop(self):
        # Check if the stack is empty.
        if not self.arr:
            return -1  # Stack is empty, return -1 as per the problem statement.
        
        # Pop and return the last element of the array (top of the stack).
        return self.arr.pop()

# Example usage:
stack = MyStack()
stack.push(2)
stack.push(3)
print(stack.pop())  # Output: 3
stack.push(4)
print(stack.pop())  # Output: 4
  