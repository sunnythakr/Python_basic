# Python Program to Find the Larger String without using Built-in Functions

s1 = input("enter first dtrings: ")
s2 = input("enter second strings: ")
s1count  = 0
s2count = 0
for i in s1:
    s1count +=1
for j in s2:
    s2count +=1

if s1count > s2count:
    print("Larger  string is: ")
    print(s1)
elif(s1count==s2count):
    print("Both the strings are equal!")
else:
    print("Larger  string is: ")
    print(s2)

