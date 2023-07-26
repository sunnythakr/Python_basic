def findMaximum(arr, n):
    if n == 1:
        return arr[0]
    
    left, right = 0, n - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Check if mid is a peak element
        if (mid == 0 or arr[mid - 1] < arr[mid]) and (mid == n - 1 or arr[mid] > arr[mid + 1]):
            return arr[mid]
        
        # If mid is not a peak, move left or right accordingly
        if mid > 0 and arr[mid - 1] > arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    # If no peak element found, return the last element
    return arr[n - 1]

# Test Example 1
arr1 = [1, 15, 25, 45, 42, 21, 17, 12, 11]
n1 = len(arr1)
print(findMaximum(arr1, n1))  # Output: 45

# Test Example 2
arr2 = [1, 45, 47, 50, 5]
n2 = len(arr2)
print(findMaximum(arr2, n2))  # Output: 50