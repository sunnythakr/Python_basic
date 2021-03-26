# class student:

#     def __init__(self,name,rollno,marks):
#         self.name = name
#         self.rollno = rollno
#         self.marks = marks

#     def display(self):
#         print("hello my name is ",self.name)
#         print(" my roll no is", self.rollno)
#         print("Total marks is ", self.marks)

# s = student("johnson",33,435)
# s.display()


# class
# In python everything is objects  to create Objects are we required some model or plan or blueprint to
# which is nothing but class


# What is object 

# physical existance of class is nothing but Object. We can create any number of objects for  class 

# What is reference variable 
# The variable which can be used to refer object is called reference variable 
# By using reference variable we can access properties and methods of object


  
# Self variable:
# self is the default variable which is always pointing to current object and
# By using self we can access instance variables and instance methods of object


# Note
# 2. Self should be the first parameter inside constructor
# def __init__(self):

# 2. self should be the first parameter inside instance methods
# def talk(self):


# Constructor Concept:
# 1. Constructor is a special methods in python
# 2. The name constructor should be __init__(self):
# 3. constructor will be executed automatically at the time of object creation
# 4. the main purpose of constructor is to decleare and initialize instance variables
# 5. Per object constructor will be execute only once 
# 6. constructor can take atleast one argument(atleast self)


# Example:
# Program to demonistrate constructor will be execute only once per object:

# class Test:

#     def __init__(self):  
#         print("constructor Execution........")

#     def talk(self):
#         print("Method execution..........")


# t1 = Test()
# t2 = Test()
# t3 = Test()
# t4 = Test()
# t1.talk()



# Program:

# class student:
#     def __init__(self,x,y,z):
#         self.name = x
#         self.rollno = y
#         self.marks = z

#     def display(self):
#         print("student name {}\nROllno{}\nmarks{} ".format( self.name,self.rollno,self.marks ))


# s1 = student("johnson",22,455)
# s1.display()

# Types of variable :

# 1. Instance Variable(Object level Variables)
# 2. static Variable(class level Variables)
# 3. Local Variable(Method level variables)

# Program:
# 1. Inside Constructor by using self Variable:

# class Employee:

#     def __init__(self):
#         self.eno = 100
#         self.ename = "johnson"
#         self.esal = 33445
    
# e =Employee()

# print(e.__dict__)




# 2. Inside instance methods by using self variable

# class Test:

#     def __init__(self):
#         self.a  =11
#         self.b = 22
#     def m1(self):
#         self.c = 33

# t1 = Test()
# t1.m1()
# print(t1.__dict__)



# 3. Outside of the class by using object reference variables

# class Test:

#     def __init__(self):
#         self.a  =11
#         self.b = 22
#     def m1(self):
#         self.c = 33

# t1 = Test()
# t1.m1()
# t1.d = 44
# print(t1.__dict__)




# How to access instance variables:
# we can access instance variables with in the class by using self variable and outside of the class by using reference variable


# class Test:

#     def __init__(self):
#         self.a = 11
#         self.b = 22

#     def m1(self):
#         print(self.a)
#         print(self.b)

# t = Test()
# t.m1()




# How to delete Instance variables from the object

1. within a class we can delete instance variables as follows

        del self.variablename
        del self.a  # "a " is variable 


2. From Outside of a class we can delete instance variables as follows
        del objectreference.variablename
        del t.a # here t is object reference   "a" is variable 


class Test:

    def __init__(self):
        self.a =11
        self.b = 22
        self.c = 33
        self.d = 44
        self.e = 55
        self.f = 66
    def m1(self):
        del self.d

t = Test()
print(t.__dict__)  # it wont delte here 
t.m1()
print(t.__dict__) # deleted 
del t.f
print(t.__dict__)


