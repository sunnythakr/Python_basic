# Bytes data types represent a group of byte numbers just like an array 

x = [11,22,33,44,55,66]

b = bytes(x)

for i in b: 
    print(i)

print(type(b))

# ValueError: bytes must be in range(0, 256)
# the only allowed value for bytes data types are 0 to 256


