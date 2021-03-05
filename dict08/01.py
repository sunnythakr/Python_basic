# Duplicate keys are not allowed 
# Hetrogeneous objects are allowed for both ket and value
# Dictionary are mutable 
# indexing and slicing concepts are not allowed 

#  how to  create a dict 
# d= {} or d =dict{}

d=  {100:'john' , 111:'sons'}
print(d)
print(type(d))

d[234] ="john"
d[222]="brown"

print(d)

# how to update Dictionary
d=  {100:'john' , 111:'sons'}
print(d)

d[100]='Brown'

print("after updation",d)

d=  {100:'john' , 111:'sons',123:'brown',121:'Shown '}

print("Before deletion",d)

del d[100]

print("after delete the dict value",d)

print()

# clear() to remove the all value from dictionary 

print(d)

d.clear()

print("using the clear() remove all the element ")


# d= dict{}  It create the empty dictionary 


# get() To get the value associated with the key 


d=  {100:'john' , 111:'sons',123:'brown',121:'Shown '}


print(d.get(100))
print(d.get(111))
print(d.get(123))

# pop() It remove the entry associated with the specified key and returns the corresponding value 


d=  {100:'john' , 111:'sons',123:'brown',121:'Shown '}

print(d.pop(100))
print("using the pop() function " )

print(d)


# popitem() It removes an arbitrary item(key-value) from the dictionary and return it 

d=  {100:'john' , 111:'sons',123:'brown',121:'Shown '}

print(d)
print(d.popitem())

print(d)

# keys() It return all keys associated with dictionary 

d=  {100:'john' , 111:'sons',123:'brown',121:'Shown '}

print(d.keys())
for k in d.keys():
    print(k)


# values() It returns all the values associated with the dictionary 


d=  {100:'john' , 111:'sons',123:'brown',121:'Shown '}

print(d.values())
for k in d.values():
    print(k)



# items() It returns list of tuples representing key-value pairs 

d=  {100:'john' , 111:'sons',123:'brown',121:'Shown '}

for k, v in d.items():

    print(k  ,  v)


# Write a program to take dictionary from the keyboard and print the sum of values 

d= eval(input("ENter dictionary "))
s = sum(d.values())
print("sum=",s)