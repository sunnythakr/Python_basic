# Python program to check whether the string is Symmetrical or Palindrome
def palindrome(strings):
    rev_str = ""
    for i in range(len(strings)-1, -1, -1):
        rev_str +=strings[i]
    if  strings == rev_str:
            print("this is palindrome strings: ")
    else :
            print("this is not a palindrome strings: ")

def Symmetrical(strings):
    mid  = len(strings)//2
    left = strings[:mid]
    right  = strings[mid:]
    if left == right:
        print("this is a symmetrical: ")
    else:
        print("this is not a symmetrical : ")


strings = input("Enter the strings: ")
print(palindrome(strings))
print(Symmetrical(strings))