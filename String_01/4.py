# This is a Python Program to replace all occurrences of ‘a’ with ‘$’ in a string.

def replaceString(string):
   string=string.replace('a','$')
   string=string.replace('A','$')
   return string


string = input("enter a string")
print(replaceString(string))
