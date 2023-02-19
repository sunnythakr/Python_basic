# Python Program to Swap the First and Last Element in a List
lst = []
n_d = []
n = int(input("Enter the numbers of element: "))
for i in range(1, n+1):
    num = int(input("Enter number: "))
    lst.append(num)
lst.sort()
swp = lst[0]
lst[0] = lst[-1]
lst[-1] = swp
print(lst)