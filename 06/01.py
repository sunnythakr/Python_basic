# tuple is same as List except that it is immutable  i.e once we created that object we can
# not perform any changes Hence tuple is read only version 

t= 11,22,33,44  # we can write inside Round Bracket (1,2,3,4) or like this t= 1,2,3,4
print(t)
print(type(t))

t= (11,22,3,44)

print(t)
print(type(t))

# By using index 
t = (11,22,33,44,55)
print(t[1])
print(t[2])
print(t[3])


# By using slice Operator 

t= (11,22,33,4,5,66,7)
print(t[1:3])
print(t[1:4])
print(t[:4])

# mathematical Operator for tuple 
t= (11,22,33,44,)
t2 = (55,66,77)
t3 = t+t2
print(t3)


# important function of tuple 
t= (11,22,33,4,45,6,7,98,99)
print("number of element ", len(t))

t= (11,22,33,4,45,6,7,98,99) 
print("count value ",t.count(22))

t= (11,22,33,11,11,4,45,6,7,98,99)  # first element of occurance 
print("index Value ",t.index(11))


t= (11,22,33,4,45,6,7,98,99) # sort() it will sort the elementy in ascending order 
print(sorted(t))


t= (11,22,33,4,45,6,7,98,99)
print("minimum mnumber ",min(t))
print("maximum  mnumber ",max(t))


# Tuple pickling and unpickling 

a =11
b =22
c= 33
d= 54
t= a,b,c,d
print("packing a group of variable ",t) #  Here a,b,c,d are packed into a tuple t nothing but tuple packing 


t =(11,22,33,44)
a,b,c,d = t  # tuple unpacking is the reverse process 

print("a=",a,"b=",b,"c=",c,"d=",d)



# Tuple Comprehension 

t= (x*x for x in range(1,6))
print(type(t))
for t1 in t :
    print("tuple comprehension ",t1 , end="  ")
