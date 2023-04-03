# Given an integer array and another integer element. 
# The task is to find if the given element is present in array or not.
class solution:
    def search(self, arr, N, x):
        for i in range(N):
            if arr[i] == x:
                return i
        return -1
s = solution()
arr = [1,2,3,4]

N = len(arr)
x = 3
print(s.search(arr,N,x))