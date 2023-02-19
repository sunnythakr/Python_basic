# Python Program to Find Largest Number in a List
lst = []
n = int(input("Enter the numbers of element: "))
for i in range(1, n+1):
    b = int(input("Enter the numbers: "))
    lst.append(b)
lst.sort()
print("The biggest number is: ")
print(lst[-1])