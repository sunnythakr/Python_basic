# Sort a stack
class Solution:
    # Function to sort the stack such that the top element is the maximum.
    def Sorted(self, s):
        if not s:
            return
        
        # Temporary stack to hold sorted elements.
        temp_stack = []
        
        while s:
            # Pop the top element from the original stack.
            temp = s.pop()
            
            # Move elements from the temporary stack to the original stack
            # until we find the correct position for the popped element.
            while temp_stack and temp_stack[-1] < temp:
                s.append(temp_stack.pop())
            
            # Place the popped element in the correct position in the temporary stack.
            temp_stack.append(temp)
        
        # Copy elements from the temporary stack back to the original stack to sort it.
        while temp_stack:
            s.append(temp_stack.pop())

# Example usage:
stack = [3, 2, 1,9,11]
solution = Solution()
solution.Sorted(stack)

# Print the sorted stack.
while stack:
    print(stack.pop(), end=" ")  # Output: 11,9,3 2 1
