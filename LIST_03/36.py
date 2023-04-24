# Given an array of size N containing only 
# 0s, 1s, and 2s; sort the array in ascending order.
# Example 1:

# Input: 
# N = 5
# arr[]= {0 2 1 2 0}
# Output:
# 0 0 1 2 2
# Explanation:
# 0s 1s and 2s are segregated 
# into ascending order.


def sort012(arr,n):
        # code here
        count_0 = 0
        count_1 = 0
        count_2 = 0
        
        # Count the number of 0s, 1s, and 2s in the array
        for i in range(n):
            if arr[i] == 0:
                count_0 += 1
            elif arr[i] == 1:
                count_1 += 1
            else:
                count_2 += 1
        
        # Fill the array with 0s, 1s, and 2s in ascending order
        for i in range(count_0):
            arr[i] = 0
        for i in range(count_0, count_0+count_1):
            arr[i] = 1
        for i in range(count_0+count_1, n):
            arr[i] = 2
        return arr

arr= [0 ,2 ,1 ,2 ,0]
n = len(arr)
j  = sort012(arr,n)
print(j)





