# The program takes a string and removes the nth index character from the non-empty string

def removeString(string , n):
    res = ""
    n1 = len(string)
    for i in range(0,n1):
        if(i+1 == n):
            res = res+""
        elif(i+1 != n):
            res = res+string[i]
    return res

string =input("Enter a string")
n =int(input("Enter a index number you want to remove in string"))
print(removeString(string,n))             
