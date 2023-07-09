# here is a triplet (a, b, c) that satisfies a2 + b2 = c2, otherwise false.
# N = 5
# Arr = [3, 2, 4, 6, 5]
# Output: Yes
# Explanation: a=3, b=4, and c=5 forms a
# pythagorean triplet.

def checkTriplet(arr, n):
    # Square all elements in the array
    arr = [x * x for x in arr]

    # Sort the squared array in ascending order
    arr.sort()

    for i in range(n - 1, 1, -1):
        j = 0
        k = i - 1
        while j < k:
            if arr[j] + arr[k] == arr[i]:
                return True
            elif arr[j] + arr[k] < arr[i]:
                j += 1
            else:
                k -= 1
    return False

arr = [3, 8, 5]
n = len(arr)
print(checkTriplet(arr,n))