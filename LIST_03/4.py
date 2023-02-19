# Python Program to Split Even and Odd Elements into Two Lists
lst = []
even = []
odd = []
n = int(input("please enter number of element: "))
for i in range(1,n+1):
    num = int(input("Please enter the number: "))
    lst.append(num)
for l in lst:
    if l%2==0:
        even.append(l)
    else:
        odd.append(l)
print("Even number list: ")
print(even)
print("Odd number list: ")
print(odd)


