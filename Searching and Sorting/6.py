def countZeroes(A, N):
    row, col = 0, N - 1
    count = 0

    while row < N and col >= 0:
        # If the current element is 0, it means the entire column from this point downwards will have zeros
        if A[row][col] == 0:
            count += col + 1
            row += 1
        # If the current element is 1, move left in the same row to find the first zero
        else:
            col -= 1

    return count

# Test cases
A1 = [[0, 0, 0],
      [0, 0, 1],
      [0, 1, 1]]
N1 = 3
print(countZeroes(A1, N1))  # Output: 6

# A2 = [[1, 1],
#       [1, 1]]
# N2 = 2
# print(countZeroes(A2, N2))  # Output: 0
