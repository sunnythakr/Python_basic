# We can use identity operator for address comparison 

a = 11
b  = 11

print(a is b)

print(id (a))
print(id (b))

lst1 = ['john','son']
lst2 = ['john','son']

print(lst1 is lst2)  # always goes to check address operator this   'is ' operator 