# Given a string S consisting only '0's and '1's,  find the last index of the '1' present in it.
# Input:
# S = 00001
# Output:
# 4
# Explanation:
# Last index of  1 in given string is 4.

def lastindex(s):
    for i in range(len(s) - 1, -1, -1):  # Iterate from right to left
        if s[i] == '1':
            return i
    return -1  # If '1' is not present, return -1

# Test cases
print(lastindex("00001"))  # Output: 4
print(lastindex("0"))      # Output: -1