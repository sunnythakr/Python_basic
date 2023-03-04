# Python | Ways to find length of list

lst = []
n = int(input("Enter the number of element: "))
for i in range(n):
    num  = int(input("Enter the element: "))
    lst.append(num)
counter = 0
for l in lst:
    counter +=1
print(lst,)
print("the length of list is! ", counter)



