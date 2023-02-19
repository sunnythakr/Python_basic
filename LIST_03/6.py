# Python Program to Print Sum of Negative Numbers, Positive Even Numbers and Positive Odd numbers in a List
lst = []
sum  = 0
even_positive = []
sum_even_positive =0
odd_positive = []
sum_odd_positive = 0
negative = []
sum_negative = 0
n = int(input("Enter the number of element: "))
for i in range(1, n+1):
    num = int(input("Enter the number: "))
    lst.append(num)
lst.sort()
for l in lst:
    if l >=0 and l%2==0:
        even_positive.append(l)
        sum_even_positive += l
    elif l>=0 and l%2!=0:
        odd_positive.append(l)
        sum_odd_positive +=l
    else:
        negative.append(l)
        sum_negative +=l
print("Even positive: ")
print(sum_even_positive)
print("Odd positive: ")
print(sum_odd_positive)
print("Negative: ")
print(sum_negative)