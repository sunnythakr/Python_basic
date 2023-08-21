# list is a mutable data types 

lst = [11,22,33,44,5,56]

print(lst)

print('type of ',type(lst))

print(lst[0])

print(lst[4])

print(lst[:3])

lst1 = [11,22,'johnson',22.44,True]

print('this is list',lst1)

print(type(lst1))

lst1.append('listappend ') # Append always add at  end of the element 
lst1.append(11)
#  lst1.append(11,33) ==> TypeError: append() takes exactly one argument (2 given)
# if you will give the more than one argument 

print(lst1)

