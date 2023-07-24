# Given a sorted array having N elements, find the indices of the first and
#  last occurrences of an element X in the given array.
# Note: If the number X is not found in the array, return '-1' as an
# example 1 
# time complexity is O(n)
# def firstAndLast(arr, n, x): 
#         em = []
#         if arr == []:
#             return -1
#         for i in range(n):
#             if arr[i] == x:
#                 em.append(i)
#         if len(em) == 0:
#                 return -1
#         if len(em) == 1:
#                 return em[0], em[0]
#         if len(em) >= 1:
#                 return em[0], em[-1]
#         return -1
# X = 3
# arr = []
# N = len(arr)
# print(firstAndLast(arr,N,X))

# example 2
# time complexity O(log(N))

def findFirstAndLast(arr, n, x):
    def binarySearch(arr, n, x, find_first):
        left, right = 0, n - 1
        result = -1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == x:
                result = mid
                if find_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1

        return result

    first_index = binarySearch(arr, n, x, True)
    last_index = binarySearch(arr, n, x, False)

    if first_index == -1:
        return [-1]
    else:
        return [first_index, last_index]

# Test cases
print(findFirstAndLast([1, 3, 3, 4], 4, 3))  # Output: [1, 2]
print(findFirstAndLast([1, 2, 3, 4], 4, 5))  # Output: [-1]

