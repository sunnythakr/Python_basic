# Python program to print even length words in a string
str = input("Enter the strings: ")
lst = str.split()
d= []
for i in lst:
    if len(i) % 2 == 0:
        d.append(i)
print(" ".join(d))
