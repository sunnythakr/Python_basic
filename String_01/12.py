# Python Program to Count the Number of Digits and Letters in a String

string=input("Enter string: ")
digit = letter = 0
for i in string:
      if(i.isdigit()):
           digit +=1
      elif(i.isalpha()):
        letter +=1
      else:
        pass
print("The number of digits is: ",digit)

print("The number of characters is: ", letter)







