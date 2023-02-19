# Python Program to Merge Two Lists and Sort it
lst1 = []
n = int(input("Enter the numbers of element: "))
for i in range(1, n+1):
    num = int(input("Enter number: "))
    lst1.append(num)
lst2 = []
n = int(input("Enter the numbers of element: "))
for i in range(1, n+1):
    num = int(input("Enter number: "))
    lst2.append(num)
lst1.extend(lst2)
lst1.sort()
print("Sorted list is: ")
print(lst1)

# without using extend function
lst1 = []
n = int(input("Enter the numbers of element: "))
for i in range(1, n+1):
    num = int(input("Enter number: "))
    lst1.append(num)
lst2 = []
n = int(input("Enter the numbers of element: "))
for i in range(1, n+1):
    num = int(input("Enter number: "))
    lst2.append(num)
for j in lst2:
    lst1.append(j)
lst1.sort()
print("Sorted list is: ")
print(lst1)

