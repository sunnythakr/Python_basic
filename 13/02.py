# # without try_except 
# print("stmt-1")
# print(10/0)
# print("stmt-3")

# # output: 
# stmt-1
# ZeroDivisionError: Division by zero

# with try-except 
# print("stmt-1")
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print(10//2)
# print("stmt-3")


# control flow in try except
# try:
#         stmt-1
#         stmt-2
#         stmt-3
# except XXX:
#     stmt-4
# stmt-5



# how to print exception information

# try:
#     print(10/0)
# except ZeroDivisionError as msg:
#     print("Exception raised and its description is ", msg)


# try with multiple except Block 

# try:
#     x = int(input("enter first Numbers"))
#     y = int(input("enter first number"))
#     print(x/y)
# except ZeroDivisionError:
#     print("can not divide with zero")
# except ValueError:
#     print("Please provide int value only")



# Single except Block that can handle multiple exceptions

try:
    x = int(input("enter first number"))
    y = int(input("enter second numbers "))
    print(x/y)
except(ZeroDivisionError,ValueError) as msg:
    print("please Provide valid Only",msg)


# Default except Block

# try:
#     x = int(input("enter first number"))
#     y = int(input("enter second numbers "))
#     print(x/y)
# except ZeroDivisionError:
#     print("Zerodivision error ")
# except:
#     print("Default except: please provie valid  ")


# ***note  if try with multiple except block available then default except block should be last , otherwise  we will get syntaxError

try:
    print("100/0")
except:
    print("please Provide valid")
except ZeroDivisionError:
    print("zero divide error ")



