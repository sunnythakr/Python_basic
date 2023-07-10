def booleanMatrix(matrix):
    R = len(matrix)
    C = len(matrix[0])

    rowFlag = [0] * R
    colFlag = [0] * C

    # Mark the rows and columns to be modified
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 1:
                rowFlag[i] = 1
                colFlag[j] = 1

    # Modify the matrix based on rowFlag and colFlag
    for i in range(R):
        for j in range(C):
            if rowFlag[i] == 1 or colFlag[j] == 1:
                matrix[i][j] = 1

    return matrix

matrix2 = [[1, 0, 0], [1, 0, 0], [1, 0, 0], [0, 0, 0]]
print(booleanMatrix(matrix2))
# Output: [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 0, 0]]