#range is immutable data type


ran = range(11)

print(ran)

for i in ran: print(i)


for i in range(10,20):
    print(i)

for i in range(1,11,2) : # here we add step 2
    print(i, end = ',')
    print()

# we can access  the element present in the element range data types using index 

ran  = range(1,22)
print('hello this is index value of range ',ran[2])

# We can not modify the value of range \
#  ran[11]  =  100
# TypeError: 'range' object does not support item assignment



lst = list(range(11))

print(lst)