# Python program to swap two elements in a list
def swapElement(list, pos1, pos2):
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    return lst
lst = []
n = int(input("Enter the number of element: "))
for i in range(n):
    num  = int(input("Enter the element: "))
    lst.append(num)
pos1 = int(input("enter pos1 element:"))
pos2 = int(input("enter pos2 element:"))
print("new Swap element list is : ")
print(swapElement(list, pos1-1, pos2-1))



