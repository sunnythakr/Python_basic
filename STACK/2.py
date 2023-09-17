# Immediate Smaller Element
def immediateSmaller(arr, n):
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i] = arr[i + 1]
        else:
            arr[i] = -1
    arr[n - 1] = -1

# Test cases
if __name__ == "__main__":
    arr1 = [4, 2, 1, 5, 3]
    n1 = len(arr1)
    immediateSmaller(arr1, n1)
    print(arr1)  # Output: [2, 1, -1, 3, -1]

    arr2 = [5, 6, 2, 3, 1, 7]
    n2 = len(arr2)
    immediateSmaller(arr2, n2)
    print(arr2)  # Output: [-1, 2, -1, 1, -1, -1]
