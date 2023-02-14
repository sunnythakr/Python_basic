# Python Program to Map Two Lists into a Dictionary
l1 = [1,2,3,4,5,6]
l2 = ['a','b','c','d','e','f']

Dic = {}

n = int(input("enter a number :"))

for i in range(0,n):
    Dic[l1[i]] = l2[i]

print(Dic)    