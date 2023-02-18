# Python Program to Determine How Many Times a Given Letter Occurs in a String Recursively

string  = input("Please enter strings: ")
occur_str = input(" Enter the occurance string")
empty_str = []
for i in string:
    if i == occur_str:
        empty_str.append(i)
    else:
        pass
print("The occurance of strings", occur_str,"is ", len(empty_str),"times")















