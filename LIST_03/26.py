#  rotate the array by one position in clock-wise direction.
def rotate( arr, n):
    # temp variable store last element
    temp = arr[n-1]
    for i in range(n-1, 0, -1):
    # replace the last two element 
        arr[i] = arr[i-1]
    # assign first element to temp
    arr[0] = temp
    return arr

arr = [1, 2, 3, 4, 5]
n = len(arr)
print("Original array: ", arr)
print(rotate(arr,n))