# Bytearrya are mutable 
# there is  difference between mutable and immutable  once we Create the Objects we can not perform any changes 
# in that object this is called non changeable behaviour immutability 

x = [11,22,33,44,55,66]
b = bytearray(x)

print(type(b))

for i in b:
    print(i)


b[0] = 111 # this is immutable  you can add the value 

for i in b: print(i , end = ',')