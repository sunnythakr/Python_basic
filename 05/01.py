# Create Empty List 
list =[]
print(list)
print(type(list))

# Dynamic input 
list = eval(input("Enter List "))  # enter input like this [11,2,33,44]
print(list)
print(type(list))    

# With split function 
s=  'learning python is very easy '  # split() convert the element into list 
d = s.split()
print(d)
print(d)

# append() Function
list = []            # append add the element at the end of list  but one element at a time 
for i in range(101):
    if i%10==0:
        list.append(i)
print(list)

# insert() Function 
ins = [11,22,33,44,55] # insert() you have to mention index value where do you want insert value  
print(ins)
ins.insert(0,7643)
print('commit changes ',ins)


#extends Function
x= [11,22,33]
y=[44,55,66]
x.extend(y) # here you have to mention which file/element is extending with y like here "x"
print('extended    ', x)

# Remove () function 
lst =[11,22,33,44,55] # in remove function which element you want to remove you have to do that 
lst.remove(44)

print(lst )

# pop() function 
ls = [11,22,33,44,55,66,77,88,99]
print(ls)
ls.pop()   # it remove at the end of an element 
print('after pop element ',ls)
ls.pop()
print('after pop one more element ',ls)




# Reverse()  function 

n = [11,22,33,44,55,66,77]
n.reverse()
print(n)



#  sort() function 
srt = [22,33,77,21,0,33,9,56,4]
srt.sort()
print(srt)  

s= ['dog','banaba','apple ']
s.sort()
print(s)