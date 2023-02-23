# Python Program to Return the Length of the Longest Word from the List of Words
lst =[]
sum1 = 0
h=0
ls = []
n = int(input("Enter the numbers of element: "))
for i in range(1, n+1):
    num = input("Enter number: ")
    lst.append(num)
for i in lst:
    for j in i:
        sum1  = sum1 + 1
    if sum1>h:
        ls.append(i)
        h = sum1
    sum1 = 0 
print(ls[-1])


