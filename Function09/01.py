# # # If a group of statements is repeatedly required then it is not recommended to write 
# # these statements everytime seperately we have to define these statements as a single units 
# # and we can call that unit any number of times bases on our requirements without rewriting .
# # this unit is nothing but function 


# # python support two types of function 

# # 1. Built in function 

# eg:

# id()
# type()
# input()
# eval()
# etc.....


# # 2. User define Function
# # 
# # def function_name(parameters):
# #   return Value 





# Write a function to take name of the student as input and print wish messages by name 

def wish(name):
    print("hello",name, "good morning ")

wish("john")
wish("sons")


# Write a functionn  to take number as input and print square value

def square(number):
    print("the square of ",number ,"is ", number*number)

square(4)
square(5)
square(6)

# write a function to accept 2 numbers as input and return sum 

def add (x,y):
    return x+y

print("the sum is ", add(11,22))


# Write a fuction to check wheateher the given number is even or odd 


def even_odd(number):
    if number%2==0:
        print(number,"This is a even number ")

    else:
        print(number ,"this is a odd number ")

even_odd(11)
even_odd(12)
even_odd(101)


# Write a function to find factorial of given number 

def fact(num):
    result = 1
    while num>=1:
        result = result*num
        num =num-1
    return result

for i in range(1,5):
    print("ths factorila of ",i,"is",fact(i))



# return multiple value from a function 

def sum_sub(a,b):
    sum = a+b
    sub = a-b
    return sum,sub
a,b=sum_sub(100,50)
print("the sum is ",a)
print("the sub is ",b)

# Example we can pass argument value by keyword that is parameter name 

def wish1(name,msg):
    print("hello",name,msg)
    
wish1("sunny","how are youn")
wish1(name ="sunny",msg="how are youn")


# degfault Argument

def default(name="Guest"):
    print("hello",name,"How are you")

default("johnsons")
default() #  we did not pass argument here default argument 



# Variable lenght Arguments 

def sum(*n):
    total = 0
    for n1 in n:
        total = total+n1
    print("the sum of total",total)

sum(11)
sum(11,22)
sum(11,33,44,55)
sum(11,1,12,34,56)



