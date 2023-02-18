# This is a Python Program to remove the characters of odd index values in a string.

str = input("Enter strings") 
emp_str = "" 
for i in range(len(str)):
    if i%2 == 0:
        emp_str = emp_str + str[i]
    else:
        pass
print(emp_str)
