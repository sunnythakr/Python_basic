# syntax x = =first Value if condition else second value 

a,b =11,22

x= 33 if a>b else 44  

print(x)


# Read the two number from the keyboard and print minimum value 

a = int(input('the the first value'))
b = int(input('the the second value'))

val = a if a<b else b

print('minumum Value is ' , val )


# Program for minimum three number 

a = int(input('the the first value'))
b = int(input('the the second value'))
c = int(input('the the third  value'))


val = a if a<b and a<c else b if b<c else c
print('minumum Value is ' , val )


