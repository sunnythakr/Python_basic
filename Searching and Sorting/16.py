# Given two arrays of length N and M, print the merged array in ascending 
# order containing only unique elements.
# Example 1
def sorttwoarray(a,b,n,m):
    merge_ab = a + b
    answer = []
    for i in merge_ab:
        if i not in answer:
            answer.append(i)
    answer.sort()
    answer_len = len(answer)
    return answer_len

# Example 2
def mergeNsort(self, a, b, n, m, answer):
    # Step 1: Merge the arrays
    merged = a + b
    
    # Step 2: Sort the merged array in ascending order
    merged.sort()
    
    # Step 3: Remove duplicates from the sorted array
    unique_elements = []
    for num in merged:
        if not unique_elements or unique_elements[-1] != num:
            unique_elements.append(num)
    
    # Update the answer array with the unique elements
    for i in range(len(unique_elements)):
        answer[i] = unique_elements[i]
    
    # Return the size of the merged and sorted array
    return len(unique_elements)

a = [7, 1, 5, 3, 9]
b = [8, 4, 3, 5, 2, 6]
# a = [1,8]
# b = [10,11]
n = len(a)
m = len(b)
print(sorttwoarray(a,b,m,n))
answer = [0] * (n + m)
print(mergeNsort(m,n,a,b,answer))

