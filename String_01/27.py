# Python – Avoid Spaces in string length
strings = input("ENter the strings: ")
count = 0
for i in range(len(strings)):
    if not strings[i] == " ":
        count +=1
print(count)
