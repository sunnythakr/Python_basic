# Given two integer arrays A1[ ] and A2[ ] of size N and M respectively.
#  Sort the first array A1[ ] such that all the relative positions of the
#  elements in the first array are the same as the elements in the second 
# array A2[ ].

def sortA1ByA2(A1, N, A2, M):
    # Step 1: Create a dictionary to store the frequency of elements in A1
    freq_dict = {}
    for num in A1:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    
    # Step 2: Create a result array to store the sorted elements
    result = []
    
    # Step 3: Iterate through A2
    for num in A2:
        if num in freq_dict:
            # Add the element to the result array the number of times it appears in A1
            result.extend([num] * freq_dict[num])
            # Remove the element from the dictionary
            del freq_dict[num]
    
    # Step 4: Sort the remaining elements in A1 that are not present in A2 and add them to the result array
    remaining = sorted(freq_dict.keys())
    for num in remaining:
        result.extend([num] * freq_dict[num])
    
    # Step 5: Return the result array
    return result

# Example 1
N = 11
M = 4
A1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
A2 = [2, 1, 8, 3]
output = sortA1ByA2(A1, N, A2, M)
print(output)  # Output: [2, 2, 1, 1, 8, 8, 3, 5, 6, 7, 9]

# Example 2
N = 11
M = 4
A1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
A2 = [99, 22, 444, 56]
output = sortA1ByA2(A1, N, A2, M)
print(output)  # Output: [1, 1, 2, 2, 3, 5, 6, 7, 8, 8, 9]
