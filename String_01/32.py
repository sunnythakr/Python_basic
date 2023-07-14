def remAnagram(str1, str2):
    count1 = [0] * 26
    count2 = [0] * 26

    # Count the frequency of characters in str1
    for char in str1:
        count1[ord(char) - ord('a')] += 1

    # Count the frequency of characters in str2
    for char in str2:
        count2[ord(char) - ord('a')] += 1

    # Calculate the number of characters to be deleted
    deletions = 0
    for i in range(26):
        deletions += abs(count1[i] - count2[i])

    return deletions

# Example usage:
str1 = "bcadeh"
str2 = "hea"
result = remAnagram(str1, str2)
print(result)  # Output: 3
