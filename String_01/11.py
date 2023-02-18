# Python Program to Count Number of Uppercase and Lowercase Letters in a String

string = input("enter strings")
store_srings = "abcdefghijklmnopqrstuvwxyz"
upper_count = 0
lower_count = 0
for i in string:
    if i in store_srings:
        lower_count +=1
        print("lower",lower_count)
    else:
        upper_count =upper_count+ +1
        print("upper",upper_count)

print(" Number of Uppercase Letters in a String: ", upper_count)
print(" Number of Lowercase Letters in a String: ",lower_count)





