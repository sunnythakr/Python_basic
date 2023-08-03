# Given a matrix of size n x m, where every row and column is sorted in 
# increasing order, and a number x. Find whether element x is present
#  in the matrix or not.

def search(matrix, n, m, x):
    # Starting from the top-right corner of the matrix
    i, j = 0, m - 1

    while i < n and j >= 0:
        if matrix[i][j] == x:
            return True
        elif matrix[i][j] > x:
            # Move left if the current element is greater than the target value
            j -= 1
        else:
            # Move down if the current element is smaller than the target value
            i += 1

    # If we reach here, the target value is not present in the matrix
    return False

# Test Example 1
matrix1 = [
    [3, 30, 38],
    [36, 43, 60],
    [40, 51, 69]
]
n1, m1, x1 = 3, 3, 62
print(search(matrix1, n1, m1, x1))  # Output: False

# Test Example 2
matrix2 = [[18, 21, 27, 38, 55, 67]]
n2, m2, x2 = 1, 6, 55
print(search(matrix2, n2, m2, x2))  # Output: True
