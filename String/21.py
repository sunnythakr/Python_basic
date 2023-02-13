# Python Program to Count Number of Vowels in a String

strings = input("Enter the strings: ")
count = 0
for i in strings.lower():
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count +=1
    else:
        pass
print("Numbers of vowels is: ")
print(count)





