# it is mutable data type 
# Duplicates values are not allowed 

s = {11,22,33,33,44,44,55,66,66,66,77,6}  # gives you the unordered output

print(type(s))


print('this is set',s )


#s[0] =11
#TypeError: 'set' object does not support item assignment

s.add('johnson') # It wont be add the element  at the end randomly add the set

print('element added ',s)  

s.remove(77)

print('element romoved ',s)






























