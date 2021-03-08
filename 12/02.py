# The" With "statement you dont need to worry about close() file it will take care of that

with open("ccb.txt", 'w') as f:
    f.write("hello\n")
    f.write("openting the file \n with statements ")
print("is file closed ", f.closed)


# The seek() and tell() method

# we can use tell method to return position of the cursor (file pionter ) from beginning of the file
# The position (index ) of first character in files is zero just like string index

with open("abc.txt", 'r') as f:
    print(f.read(2))
    print(f.tell())
    print(f.read(4))
    print(f.tell())

    # we can use seek() method to move cursor (file pointer) to specified location

data = "All student are stupid  "
f = open("acc.txt", "w")
f.write(data)
with open("acc.txt", "r+") as f:
    text = f.read()
    print(text)
    print("The current cursor Position ", f.tell())
    f.seek(17)
    print("the current cursor position ", f.tell())
    f.write("GEMS!!!")
    f.seek(0)
    text = f.read()
    print("data after modification")
    print(text)
    # write a program to check wheather the given file exists or not exosts. if it is availabel print its content

import os,sys
fname = input("ENter the file name ")
if os.path.isfile(fname):
    print("path exists", fname)
    f=open(fname,'r')
else:
    print("the file does not exisrt ", fname)
    sys.exit(0)

print("the content of file is ")
data = f.read()
print(data)



# Write  data to csv file 

import csv
with open("emp.csv" "w") as f :
    w = csv.writer(f)
    w.writerow(['ENO','ENAME','ESAL','EADDR'])
    n=int(input("ENter number of employee"))
    for i in range(n):
        eno = input("enter employee number ")
        ename  =input("enter emp name")
        esal = int(input("enter empliyee salary"))
        eaddr  = input("enter employee address")
        w.writerow([eno,ename,esal,eaddr])

print("total data written to the csv file sucessfully ")