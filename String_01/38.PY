def longestSubstrDistinctChars(S):
    n = len(S)
    max_length = 0
    start = 0
    char_dict = {}

    for end in range(n):
        if S[end] in char_dict:
            start = max(start, char_dict[S[end]] + 1)
        
        char_dict[S[end]] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length

S = "geeksforgeeks"
print(longestSubstrDistinctChars(S))
