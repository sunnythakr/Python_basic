def countOccurence(arr, n, k):
    threshold = n // k  # Calculate the threshold for elements to be counted

    freq_map = {}  # Dictionary to store frequency of elements

    # Count the frequency of each element in the array
    for num in arr:
        freq_map[num] = freq_map.get(num, 0) + 1

    # Find elements that appear more than n/k times
    count = 0
    for freq in freq_map.values():
        if freq > threshold:
            count += 1

    return count

# Test cases
print(countOccurence([3, 1, 2, 2, 1, 2, 3, 3], 8, 4))  # Output: 2
print(countOccurence([2, 3, 3, 2], 4, 3))            # Output: 2
