# list comprehension 

s =[x*x for x in range(1,11)]
print(s)

t= [2**x for x in range(1,5)]
print(t)

#example 

words = ["sunny",'bunny','chinny',"Munny"]
l = [w[0] for w in words]
print(l)

# example 
num1 = [11,22,33,44]
num2 = [55,66,77,88]

#Example 
words = "the quick brown box for jumps over the lazy dog ".split()
print(words)
l = [[w.upper(),len(w)]for w in words]
print(l)

# write a program to display unique vowels present in the given words

vowels = ["a","e","i","o","u"]
words = input("please enter the words ")
found = []
for letter in words:
    for letter in vowels:
        if letter not in found:
            found.append(letter)

print(found)
print("the number of different vowels present in",words,"is",len(found))