# if 

name  = input('enter the name')
if name == 'jonh':
    print('hello john welcome to loop ')
print('how are you')



# if-else 

name  = input('enter the name')
if name == 'jonh':
    print('hello john welcome to loop ')
else :
    print('hello unknown person welcome to loop')
print('how are you ')


# if-elif-else:

brand = input ('enter your favourite clothing brand ')
if brand == 'A':
    print('This is my favoyrite brand A')
elif brand == "B":
    print('this is my favourite brand B ')
elif brand =='C':
    print('this is my favourite Berand  C ')
else:
    print('this categories is not a Brand ')


    # Write a program to find boggest of given two number from the command prompt
    a = int(input('enter the first number '))
    b = int(input('enter the second number '))
    if a>b :
        print('the Biggest number is ', a)
    else:
        print('the Biggest number is ', b)
    


# Writw a program to find of given 3 numbers from the command prompt

a = int(input('enter the first number '))
b = int(input('enter the second number '))
c = int(input('enter the third number '))

if a>b and a>c :
    print('the biggest number is a= ', a)
elif b>c:

    print('the biggest number is b= ', b)
else:
    print('the biggedt number is c= ', c)


# write a progrma to find smallest of given two number \

a = int(input('enter the first number '))
b = int(input('enter the second number '))
if a<b :
        print('the smallest number is a=', a)
else:
        print('the smallest number is b= ', b)


# Write A program to check whether the given number is odd or even 

number = int(input('please enter the number '))
if number%2==0:
    print('this is even number ', number )
else:
    print('this is Odd number ', number )





# for loop 
num = 'johnson'
for i in num:
    print(i)

# To print character present in string index wise 

char = input('please Enter the String')
i = 0
for c in char:
    print("the character present at",i,"index is ",c)
    i=i+1


# to Print hello 10 times 
for i in range(10):
    print("hello")



# to display numbers from 0 to 10
for x in range(10):
    print(x)

# to display odd number from 0 to 20

for d in range(21):
    if(d%2!=0):
        print(d)

# to display number from 10 to 1 in  descending order 
for x in range(10,1,-1):
    print(x)