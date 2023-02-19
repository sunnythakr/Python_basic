# Python Program to Find Second Largest Number in a List
lst = []
n = int(input("Enter the numbers of element: "))
for i in range(1, n+1):
    num = int(input("Enter the numbers: "))
    lst.append(num)
lst.sort()
print("Sorted Numbers: ")
print(lst)
print("Second Largest number is: ")
print(lst[-2])





