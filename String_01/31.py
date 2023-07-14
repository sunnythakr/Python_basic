# Input:
# N = 5
# S = 01101
# Output: 3
# Explanation: There 3 substrings from the
# given string. They are 11, 101, 1101.
def binarySubstring(n, s):
    count = 0

    for i in range(n):
        if s[i] == '1':
            count += 1

    return count * (count - 1) // 2

# Example usage:
n = 5
s = "01101"
result = binarySubstring(n, s)
print(result)  # Output: 6