# Find the count of all the 0's.
# example 1
def countZeroes(arr, n):
        return arr.count(0)

# example 2
def countZeroes(arr, n):
        count = 0
        for i in range(0,n):
            if arr[i] == 0:
                count +=1
        return count

print(countZeroes([1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], 12))  # Output: 3
print(countZeroes([0, 0, 0, 0, 0], 5))                      # Output: 5