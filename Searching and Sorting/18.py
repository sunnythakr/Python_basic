#   find the smallest positive number missing from the array.
 
 # Helper function to perform cyclic sort
def missingNumber(self, arr, n):
    def cyclicSort(arr, n):
        i = 0
        while i < n:
            if 1 <= arr[i] <= n and arr[i] != arr[arr[i] - 1]:
                arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
            else:
                    i += 1

        cyclicSort(arr, n)

        # Find the first index where the element doesn't match its value (missing number)
        for i in range(n):
            if arr[i] != i + 1:
                return i + 1

        # If all elements are in the correct position, the missing number is N + 1
    return n + 1