# Length of Last Word
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

def lengthOfLastWord(s):
        sp = s.split()
        for i in range(len(sp)-1, -1,-1):
            return(len(sp[i]))
            break
w = "hello world"
print(lengthOfLastWord(w))
