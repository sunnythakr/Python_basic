# Python Program to Count Number of Lowercase Characters in a String

string = input("enter string")
store_char = "abcdefghijklmnopqrstuvwxyz"

count= 0
for i in  string:
    if i in store_char:
        count +=1
    else:
        pass

print("The number of lower char is: ",count)
