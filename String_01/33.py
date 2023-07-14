def merge(S1, S2):
    merged_string = ''
    len1 = len(S1)
    len2 = len(S2)
    i = 0
    j = 0

    # Merge the strings alternatively until one of them reaches the end
    while i < len1 and j < len2:
        merged_string += S1[i] + S2[j]
        i += 1
        j += 1

    # Add the remaining characters from the longer string, if any
    merged_string += S1[i:] + S2[j:]

    return merged_string

# Example usage:
S1 = "Hello"
S2 = "Bye"
result = merge(S1, S2)
print(result)  # Output: HBeylelo

S1 = "abc"
S2 = "def"
result = merge(S1, S2)
print(result)  # Output: adbecf