# While loop 
# TO print numbers from 1 to 11 by using while loop 
x= 1
while x<=11:
    print(x ,end=':')
    x=x+1

# To display the sum of first n number

n = int(input('Enter the number '))
sum = 0
i = 1
while i<=n:
    sum=sum+i
    i=i+1
    print('the sum of first ',n,"number is sum = ",sum)

# Write a program to display *'s in right triangle form

#*
#* *
#* * *
#* * * *
#* * * * *
#* * * * * *
#* * * * * * *
#* * * * * * * *

n = int(input("enter the number of rows"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end="")
    print()


# Break Statement cd 
for i in range(11):
    if i==10:

        print("the element 10 not allowed here ")
        break
    print(i)


#example 
cart = [11,22,33,44,55,66,77]
for item in cart:
    if item==44:
        print('item 44 now allowed to be carried')
        break
    print(item, end='::')



# Continue 
# we use continue statement to skip current iteration and continue next iteration 

#example 1:: to print odd number in the range 0 to 9
for io in range(10):
    if i%2==0:
        continue
    print(i)

# example2 

cart = [11,22,33,44,55,66,77,88,99]
for item in cart:
    if item==55:
        print('this item can not carry please continue')
        continue
    print(item)

# example3
# pass statement \
# pass is keyword in python 
for i in range(100):
    if i%9==0:
        print(i)
    else:
        pass