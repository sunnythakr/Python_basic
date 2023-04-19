# Given an unsorted array A of size N that contains only positive integers,
#  find a continuous sub-array that adds to a given number S and return the
#  left and right index(1-based indexing) of that subarray.

# In case of multiple subarrays, return the subarray indexes which come first on
#  moving from left to right.

def subArraySum(arr, n, s): 
       #Write your code here
        left = right = curr_sum = 0
        
        while right < n:
            curr_sum += arr[right]
            
            while curr_sum > s:
                curr_sum -= arr[left]
                left += 1
            
            if curr_sum == s:
                return [left+1, right+1]
            
            right += 1
        
        return [-1]
s =12
arr  = [1,2,3,7,5]
n = len(arr)
print(subArraySum(arr,n,s))