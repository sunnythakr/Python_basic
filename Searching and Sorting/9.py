def matSearch(mat, N, M, X):
    # Start from the top-right corner of the matrix
    row = 0
    col = M - 1

    while row < N and col >= 0:
        # If the current element is equal to X, return 1
        if mat[row][col] == X:
            return 1
        # If the current element is greater than X, move left
        elif mat[row][col] > X:
            col -= 1
        # If the current element is smaller than X, move down
        else:
            row += 1

    # If X is not found in the matrix, return 0
    return 0


# Example 1
mat1 = [
    [3, 30, 38],
    [44, 52, 54],
    [57, 60, 69]
]
N1, M1 = 3, 3
X1 = 62
print(matSearch(mat1, N1, M1, X1))  # Output: 0

# Example 2
mat2 = [[18, 21, 27, 38, 55, 67]]
N2, M2 = 1, 6
X2 = 55
print(matSearch(mat2, N2, M2, X2))  # Output: 1
