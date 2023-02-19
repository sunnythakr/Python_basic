# Python Program to Remove Duplicates from a List
lst = []
n_d = []
n = int(input("Enter the numbers of element: "))
for i in range(1, n+1):
    num = int(input("Enter number: "))
    lst.append(num)
# lst.sort()
# n_d = (list(set(lst))) # using function 
# n_d.sort()
# print("List withoiut duplicate number: ")
# print(n_d)
# without using function
for i in lst:
    if i not in n_d:
        n_d.append(i)
n_d.sort()
print("List withoiut duplicate number: ")
print(n_d)