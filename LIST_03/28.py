# Given a binary array A[] of size N. The task is to arrange the array in increasing order.
# Note: The binary array contains only 0  and 1.
class Solution:
    def binSort(self, A, N):
        # Count the number of 0s in the array
        zeros = A.count(0)

        #first zeros elements of the array with 0s
        for i in range(zeros):
            A[i] = 0
         
        # remaining elements of the array with 1s
        for i in range(zeros, N):
            A[i] = 1
            print(A[i])

        return A

arr = [1, 0, 1, 1, 0]
n = len(arr)
sol = Solution()
sortedArr = sol.binSort(arr, n)
print("Sorted array:", sortedArr)
