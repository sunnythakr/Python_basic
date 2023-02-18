# Python Program to Check if a String is a Pangram or Not

s =["abcdefghijklmnopqrstuvwxyz"]
st = input("enter a string")
Flag  = False
for i in st:
    if i.lower() in s:
        Flag = True
    else:
        Flag = False

if Flag == True:
    print("yes")
else:
    print("no")
