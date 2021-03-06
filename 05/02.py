# Aliasing and cloning of list objects 
x = [11,22,33,44]
y = x
print(id(x))
print(id(y))
# here is the problem occur if you do changes in y it will reflect original element

y[1]= 999

print(x)

# TO overcome this problem we should go for cloning 

# the process of creating exectly duplicate independent object is called cloning 

#we implemented using slice operator or using  copy() function 


# by using slice operator
x= [1,2,3,4]
y = x[:]
y[1] =893

print(x)
print(y)


# by using copy() function 

x = [1,2,3,4,5]
y = x.copy()
y[1] = 989

print(x)
print(y)

# difference betwwen =operator and copy()
# operator meant  for aliasing and copy() means cloning

# concatenation operation 
a= [11,22,33]
b= [44,55,66]
c= a+b
print('concat the element ', c)


# Repetation Operator 

x =[11,22,33]
y = x*3

print("repetation operator ",y)


# clear() function 
x  = [11,22,33,44]
print(x)
x.clear()
print("now element using clear()",x)


# Nested List  List inside the list 

x = [11,22,[33,44]]
print("nested list ",x)
print(x[2])
print(x[2][0]) # print element  list inside  the list  
print(x[2][1]) # print element  list inside  the list  