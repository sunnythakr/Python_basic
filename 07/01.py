# collection of unorderred value if we  want to group of unique values as a single entity we 
# go for the set 
# Duplicates are not allowed 
# indexing and slicing are not allowed for the set 
# SEt objects are mutable 
# represent the curly bracket with comma , 

s ={11,11,22,33,44,55}
print(s)  # print unorder element 
print(type(s))
print(sorted(s))   # sorted use


s= set(range(1,6))
print("range in set  ",s)


# add element in set mutable behaviour 

s ={11,22,33}
print(s)
s.add(55)
print("after added the element ",s)


# update the set 

s= {11,22,33,44}

l =[66,77,88,99]
s.update(l,range(5))
print("after update the element  ",s)


# s.add(11,22,33) 
# TypeError: add() takes exactly one argument (3 given)

#    s.update(21)
# TypeError: 'int' object is not iterable


s= {11,22,33,44,55,66,77,88}
print("element of s")
s.pop()
print("after the popping element ",s )
s.pop()
print("after the popping element ",s )
s.pop()
print("after the popping element ",s )
s.pop()
print("after the popping element ",s )
s.pop()
print("after the popping element ",s )

# remove()


s={11,22,33,44,55,66,77}
print(s)
s.remove(33)

print("after the remove ",s)


# discard it remove the specify element from the set if element not present the it won't get any error 

s = {11,222,33,44}
s.discard(878)
print("element discareded",s)


# clear() 
s = {11,22,33,44,55}
print("before element ",s)

s.clear()
print('after using clear function',s)



# Union x.union(y)

x= {11,22,33,44}
y = {11,22,66,77,88}
print("element using union ",x.union(y))


# inersection() return common element in both 


x= {11,22,33,44}
y = {11,22,66,77,88}

print("common value in both ",x.intersection(y))



# differenec() return the element present ix but mot in y 
# x.difference(y) or (x-y)


x= {11,22,33,44}
y = {11,22,66,77,88}
print("present x not in y",x.difference(y))



# symmetric_difference () :
# return element present in either x or y but not in both 
# x.symmetric_difference(y) or x^y


x= {11,22,33,44}
y= {11,22,66,77,88}
print("not common in both ",x.symmetric_difference(y))




# set comprehension

s = {x**x for x in range(1,11)}
sorted(s)
print(s)



# Write a program to eleminate duplicates in the list 
i = eval(input("enter the element list  "))
s=set(l)
print(s)