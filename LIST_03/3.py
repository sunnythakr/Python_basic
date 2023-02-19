# Python Program to Print Largest Even and Largest Odd Number in a List
lst = []
n = int(input("Enter the numbers of element: "))
for i in range(1, n+1):
    num = int(input("Enter the numbers: "))
    lst.append(num)
lst.sort()
even = []
odd = []
for d in lst:
    if d % 2 == 0:
        even.append(d)
    else :
        odd.append(d)
if even==[]:
    print("No even number present in the list:")
else:
    print("Biggest even number is: ")
    print(even[-1])
if odd==[]:
    print("No odd number present in the list: ")
else:
    print("Biggest odd number is: ")
    print(odd[-1])


