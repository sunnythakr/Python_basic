# sort uppercase and lowercase letters separately 
def caseSort(s, n):
    lower_chars = []
    upper_chars = []
    
    for char in s:
        if char.islower():
            lower_chars.append(char)
        else:
            upper_chars.append(char)
    
    lower_chars.sort()
    upper_chars.sort()
    
    sorted_str = ""
    i, j = 0, 0
    
    for char in s:
        if char.islower():
            sorted_str += lower_chars[i]
            i += 1
        else:
            sorted_str += upper_chars[j]
            j += 1
    
    return sorted_str

# Test Example 1
S1 = "defRTSersUXI"
N1 = len(S1)
print(caseSort(S1, N1))  # Output: "deeIRSfrsTUX"

# Test Example 2
S2 = "srbDKi"
N2 = len(S2)
print(caseSort(S2, N2))  # Output: "birDKs"
