# Python Program to Find Common Characters in Two Strings
FirstString = input("please enter the first string")
SecondString = input("please enter the second string")
lst = []
for i in FirstString:
    for j in SecondString:
        if i == j:
            lst.append(i)
        else:
            pass
print("the common letter are: ")
for l in lst:
    print(l)
        