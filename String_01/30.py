class Solution:
    # Function to find the maximum occurring character in a string.
    def getMaxOccurringChar(self, s):
        # Create a frequency dictionary to store the count of each character
        frequency = {}
        
        # Traverse the string and update the frequency dictionary
        for char in s:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        
        # Find the maximum frequency
        max_frequency = max(frequency.values())
        
        # Find the lexicographically smallest character with the maximum frequency
        max_char = min([char for char in frequency if frequency[char] == max_frequency])
        
        return max_char

# Example usage:
solution = Solution()
str1 = "testsample"
result1 = solution.getMaxOccurringChar(str1)
print(result1)  # Output: e