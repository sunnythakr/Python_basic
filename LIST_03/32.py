# You are given an array Arr of size N. Replace every element with the next greatest element (greatest element on its right side) in the array. Also, since there is no element next to the last element, replace it with -1.

# Example 1:

# Input:
# N = 6
# Arr[] = {16, 17, 4, 3, 5, 2}
# Output:
# 17 5 5 5 2 -1
# Explanation: For 16 the greatest element 
# on its right is 17. For 17 it's 5. 
# For 4 it's 5. For 3 it's 5. For 5 it's 2. 
# For 2 it's -1(no element to its right). 
# So the answer is 17 5 5 5 2 -1
def nextGreatest(arr, n):
    greatest_right = -1
    for i in range(n-1, -1, -1):
        temp = arr[i]
        arr[i] = greatest_right
        if temp > greatest_right:
            greatest_right = temp
    return arr

arr = [16, 17, 4, 3, 5, 2]
n = len(arr)
print(nextGreatest(arr,n))

