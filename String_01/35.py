# palindrome
# Input: S = "abba"
# Output: 1
def isPalindrome(s):
    temp = s
    rev_str = ""
    for i in range(len(s)-1,-1,-1):
        rev_str += s[i]

    if rev_str == temp:
        return 1
    else :
        return 0

s = "abba"
print(isPalindrome(s))
s = "abc" # not a palindrom
print(isPalindrome(s))