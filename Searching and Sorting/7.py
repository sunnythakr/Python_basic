# array subset of another array

def isSubset( a1, a2, n, m):
    set_a1 = set(a1)

    # Check if each element of a2 is present in the set_a1
    for element in a2:
        if element not in set_a1:
            return "No"

    return "Yes"

a1_1 = [11, 7, 1, 13, 21, 3, 7, 3]
a2_1 = [11, 3, 7, 1, 7]
print(isSubset(a1_1, a2_1, len(a1_1), len(a2_1)))  # Output: Yes

a1_2 = [1, 2, 3, 4, 4, 5, 6]
a2_2 = [1, 2, 4]
print(isSubset(a1_2, a2_2, len(a1_2), len(a2_2)))  # Output: Yes

a1_3 = [10, 5, 2, 23, 19]
a2_3 = [19, 5, 3]
print(isSubset(a1_3, a2_3, len(a1_3), len(a2_3)))  # Output: No