# Input:
# geeksforgeeks
# forgeeksgeeks
# Output: 
# 1
# Explanation: s1 is geeksforgeeks, s2 is
# forgeeksgeeks. Clearly, s2 is a rotated
# version of s1 as s2 can be obtained by
# left-rotating s1 by 5 units.

def areRotations(s1, s2):
    # Check if the lengths of s1 and s2 are equal
    if len(s1) != len(s2):
        return False

    # Concatenate s1 with itself
    temp = s1 + s1

    # Check if s2 is a substring of temp
    if s2 in temp:
        return True
    else:
        return False

# Example usage:
s1 = "geeksforgeeks"
s2 = "forgeeksgeeks"
result = areRotations(s1, s2)
print(result)  # Output: True

s1 = "mightandmagic"
s2 = "andmagicmigth"
result = areRotations(s1, s2)
print(result)  # Output: False
