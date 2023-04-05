# Given two arrays A and B of equal size N, the task is to find if given arrays are equal or not. 
class Solution:
    def check(self, A, B, N):
       
        if len(A) != len(B):
            return False

        A.sort()
        B.sort()
        for i in range(N):
            if A[i] != B[i]:
                return False
        return True
A = [2,3,4,5]
B = [3,4,5,6]
N = len(A)
S = Solution()
print()