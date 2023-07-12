#Reverse a strings
# Input:
# s = Geeks
# Output: skeeG
def reverseWord(s):
    wrd = ""
    for i in range(len(s)-1,-1,-1):
        wrd +=s[i]
    return wrd

s = "Geeks"
print(reverseWord(s))