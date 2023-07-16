def longestCommonPrefix(arr, n):
    if n == 0:
        return -1

    min_len = min(len(word) for word in arr)
    result = ""
    
    for i in range(min_len):
        current_char = arr[0][i]
        
        for j in range(1, n):
            if arr[j][i] != current_char:
                return result
        
        result += current_char
    
    return result

arr = ["hello", "world"]
n = 2
print(longestCommonPrefix(arr, n))

arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
n = 4
print(longestCommonPrefix(arr, n))
