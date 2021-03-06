# types of variable
# Global Variable and Local Variable

# The variable which are decleare outside of function are called global variable


a = 11  # Global V ariable


def f1():
    print(a)


f1()

# The variable which are decleare inside  of function are called Local  variable


def f2():
    a = 12  # Local variable
    print(a)


f2()


# Example local and global Variable

x = 987


def fn1():
    x = 654
    print("print variable", x)


def fn2():
    print("print variable", x)


fn1()  # Local  Variable  x= 654
fn2()  # Global Variable  x =987

# recursive function
# A function called itself is known as Recursive Function


def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n*factorial(n-1)
    return result

print("factorial of 4 is ",factorial(4))
print("factorial of 5 is ",factorial(5))

# Write a program to create a labmnbda functio to find square of given number 


s= lambda x:x*x
print("the square of 4 is",s(4))
print("the square of 5 is",s(5))


# lambda function sum of two given number 

l = lambda a,b :a+b
print("The sum of 10 and 20 is ",l(10,20))


# lambda function of find two  biggest two number 

l=lambda a,b : a if a>b  else b

print(l(111,2434))


# Filter() function  we use filter value from the given sequence based on some condition 

# Program to filter only even number from the list by using filter() function 

# without lambda 
list1= [11,22,33,44,55,66,77,88,99,100]
for l in list1:
    if l%2==0:
        print("even number",l)

    else:
       pass

# With lambda 

lst = [11,22,33,44,55,66,77,88,99,100]
l1 =list(filter(lambda x:x%2==0,lst))
print("using lambda function",l1)

# map() function  
l=[1,2,3,4,5,6,7,8]
l1 =list(map(lambda x:x*2,l))

print("using map function ",l1)


# function   decorator
# decorator is a function which can take a function as argument and extend its functionality 
# and return modified function with extend functionality  

# the main objective of decorator function is we can extend the functionality of existing function 
# without modified that function 

def decor(func):
    def inner(name):
        if name =="Darek":
            print("hello Darek function inside function ")
        else:
            func(name)
    return inner

@decor
def dec(name):
    print("hello",name,"this is decor functionality ")

dec("Darek")
dec("john")
dec("sons")

# how to call function with decorator and without decorator 


def decor1(func):
    def inner1(name):
        if name =="Darek":
            print("hello Darek function inside function ")
        else:
            func(name)
    return inner1

@decor
def dec1(name):
    print("hello",name,"this is decor functionality ")

decorfunction = decor1(dec1)
dec1("Darek") # decorator wont be execute 
dec1("John")  # decorator wont be execute 

decorfunction = decor1("darek")
decorfunction = decor1("johnsons")

# Generator 
# Generator is a function whoich is responsible to generate a sequence of values 
# we can write generator function just like ordinary function but it uses yield Keyword to return value 


def mygen():
    yield "A"
    yield "B"
    yield "C"

g=mygen()
print(next(g))
print(next(g))
print(next(g))
# print(next(g)) # here you will get an error Tracebak (most recent call )

# example countdown 

def countdown(num):
    print("start Countdown ")
    while(num>0):
        yield num
        num=num-1

values = countdown(10)
for x in values:
    print(x)

# to generate firts n number 


def firstn(num):
    n=1
    while n<num:
        yield n
        n=n+1  # n-n+1

f= firstn(5)
for x in f:
    print(x)