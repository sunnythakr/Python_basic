# Example 1
# time coplexity O(n)
# def floor(arr, n,x):
#     i =0
#     while(n>0):
#         if arr[i] < x:
#             return 1
#             i +=1
#         return -1
# arr = [1,2,8,10,11,12,19]
# n = len(arr)
# x = 5
# print(floor(arr,n,x))

# example 2
# time complexity  O(log N)

def findFloor( arr, N, X):
        low, high = 0, N - 1
        result = -1

        while low <= high:
            mid = low + (high - low) // 2

            # If arr[mid] is greater than X, search in the left half
            if arr[mid] > X:
                high = mid - 1

            # If arr[mid] is less than or equal to X, search in the right half and update the result
            else:
                result = mid
                low = mid + 1

        return result
arr = [1,2,8,10,11,12,19]
n = len(arr)
x = 5
print(findFloor(arr,n,x))