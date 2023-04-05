# Find the missing element from an ordered array arr[]
# Input:
# N = 6
# Arr = [2, 4, 8, 10, 12, 14]
# Output: 6
class solution:
    def findMissing(self,arr,n):
        # calculate common difference by substracting last element and first element in array by floor division
        common_diff = (arr[-1]-arr[0])//n 
        for i in range(1,n):
            expected = arr[i-1] + common_diff
            if arr[i] != expected:
                return expected
        # missing element is not found return none
        return None
arr = [2, 4, 8, 10, 12, 14]
n = len(arr)
s = solution()
print("Missing element is: ")
print(s.findMissing(arr,n))