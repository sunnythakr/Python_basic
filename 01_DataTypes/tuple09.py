# tuple data types is the same data types as list but it is immutable 
# inside parenthesis ()

tup =  (11,22,33,44,55)


print(type(tup))

print(tup)

#tup[0] = 100
#TypeError: 'tuple' object does not support item assignment
# this is immiutable 

#tup.append("john") tup.append("john")
#AttributeError: 'tuple' object has no attribute 'append'


#tup.remove(22)
#AttributeError: 'tuple' object has no attribute 'remove'
