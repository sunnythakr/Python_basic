# Python Program to Count Occurrences of Element in List
lst = []
n = int(input("Enter the number of element: "))
for i in range(1, n+1):
    num = int(input("Enter number: "))
    lst.append(num)
count = 0
count_num = int(input("enter the number to be counted: "))
for i in lst:
    if i==count_num:
        count +=1
    else:
        pass
print("Numbers of times ", count_num, "appears is : ", count)