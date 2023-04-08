# Given an array A of size N of integers. Your task is to find the minimum and maximum elements in the array.

def getMinMax( a, n):
    minVal = a[0]
    maxVal = a[0]
    for i in range(1, n):
        if a[i] < minVal:
            minVal = a[i]
        elif a[i] > maxVal:
            maxVal = a[i]
    return minVal, maxVal
    

arr = [3, 2, 1, 56, 10000, 167]
n = len(arr)
minVal, maxVal = getMinMax(arr, n)
print("Minimum value:", minVal)
print("Maximum value:", maxVal)