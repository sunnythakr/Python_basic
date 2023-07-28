#   find the smallest positive number missing from the array.
 
 # Helper function to perform cyclic sort
def missingNumber(self, arr, n):
    num_set = set(arr)
    
    # Check if 1 is missing
    if 1 not in num_set:
        return 1
    
    # Find the missing number
    for num in range(2, n + 1):
        if num not in num_set:
            return num
    
    # If all numbers from 1 to n are present, return n + 1
    return n + 1