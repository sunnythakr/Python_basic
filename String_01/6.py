# The program takes a string and reverses the string using recursion.


def reverse_str(string):
    if len(string) == 0:
        return string
    else:
         return reverse_str(string[1:]) + string[0]

string = input("enter a string")
print(reverse_str(string))

# Python Program to Reverse a String Without using Recursion

def  Reverse(string):
    if len(string) == 0:
        return string
    else:
        return string[::-1]

string = input("enter a string")
print(Reverse(string))
