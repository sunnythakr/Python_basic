# An element is called a peak element if its value is not smaller than the value of its adjacent elements(if they exists).
# Given an array arr[] of size N, Return the index of any one of its peak elements.

# Input: 
# N = 3
# arr = [1,2,3
# Possible Answer: 2
# Generated Output: 1

class Solution:   
    def peakElement(self,arr, n):
        # Code here
        if n == 1:  # Special case: array has only one element
            return 0
        
        if arr[0] >= arr[1]:  # Check if the first element is a peak
            return 0
        
        if arr[n - 1] >= arr[n - 2]:  # Check if the last element is a peak
            return n - 1
        
        # Check for peaks in the remaining elements
        for i in range(1, n - 1):
            if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
                return i

        return -1  # No peak element found