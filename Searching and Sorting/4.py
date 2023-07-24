# Given an array arr containing positive elements. A and B are two 
# numbers defining a range. The task is to check if the array contains 
# all elements in the given range.
# Input: N = 7, A = 2, B = 5
# arr[] =  {1, 4, 5, 2, 7, 8, 3}
# Output: Yes
# Explanation: It has elements between 
# range 2-5 i.e 2,3,4,5
def check_elements(arr, n, A, B):
        num_set = set(arr)

        for num in range(A, B + 1):
            if num not in num_set:
                return False

        return True
        
