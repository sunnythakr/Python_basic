x=input('enter the input ')
print(x)


#Write  a program to read two number from the keyboard and print sum

x  =  input('the the first element ')
y  =  input('the the second element ')

i = int(x)
j = int(y)

print('sum of number ' ,i+j)

# How to read multiple Values from the keyboard in a single line 

a,b  = [int(x) for x in input ('enter two number ').split()] 
print('the product is ' ,a*b)



