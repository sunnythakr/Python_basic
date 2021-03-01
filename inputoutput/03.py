# Formatted String 
# %i ===> int
# %d ==> int 
# %f ==> float 
# %s ==> string type 


a=11
b=22
c=33
print('a value is %i '%a)
print('b value is %i and c value is %d '%(b,c))



name =  'johnson'
salary = 22000
age  = 56

print('hello {} your salary is {} and age is just {}' .format(name,salary,age))
print(' hello {0} your salary is {1} and age is just {2}' .format(name,salary,age)) # another way
