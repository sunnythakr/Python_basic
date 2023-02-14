# Python Program to Check if a Key Exists in a Dictionary or Not

d = {1: "A", 2: 'B', 3:'C', 4:'D'}
Key = int(input("Enter the keys: "))
if Key in d.keys():
        print("key is presemt! value is: ")
        print(d[Key])
else:
        print("Key is not present!")