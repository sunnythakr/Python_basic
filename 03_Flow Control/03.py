# Checking membership 
s = input("enter the mian strings ")
sub = input('enter the subdtring ')
if sub in s :
    print(sub,'String found in main string  ')
else:
    print('string not found ')

# removing space from thr string 
# rstrip()====> To remlove spacee from right side 
# lstrip()====> To remlove spacee from right side 
# strip()====> To remlove spacee from both sides 


city = input('enter the city name ')
scity =city.strip()
if scity=="mumbai":
    print('hello people of mumbai')
elif scity=='delhi':
    print('hello people of mumbai')
elif scity=="Punjab":
    print('hello people of mumbai')
else:
    print('this is not not listed city ')

# count()

cnt  = 'hello python is very easy to lrarn '
print(cnt.count('o'))

#Replace()
print(cnt.replace('easy','difficult'))


# join()


# split()


# changing case of a string 

py = 'learning python is very EASY COMPARE  to others '

print(py.upper())
print(py.lower())
print(py.swapcase())
print(py.title())
print(py.capitalize())
