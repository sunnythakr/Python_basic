# Python Program to Count the Number of Words and Characters in a String
string = input("Enter strings")
len = 0
word = 1
for i in string:
    if( i== " "):
        word = word +1 
    else: 
        len = len + 1
print("length of strings", len,"length of words", word) 










