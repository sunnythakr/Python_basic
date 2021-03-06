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




