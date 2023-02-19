# Python Program to Find Average of a List

lst = []
sum  = 0
n = int(input("Enter the number of element: "))
for i in range(1, n+1):
    num = int(input("Enter the number: "))
    lst.append(num)
for i in lst:
    sum +=i
average = sum/n
print("Average :")
print(average) 


