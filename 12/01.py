# File Handlimng 

# As a part of programmoing language requirements , we have to store our data permantetly
#  for future purpose for this requirements we shoul go for files 


# tyes of files 

# 1. text file 
#      Usually we can use text file to store character data eg. abc.text

# 2. binary file 
#     store binary date images,video files, audio files etc......

# Opening a file 
#      before performing any operation (like read or write ) on the file we have to open that file 

# f =(filename, mode )
#  f= open (abc.txt, w)
#  f.close()  closing the file 



f = open("abc.txt","w")
print("file name",f.name)
print("File Mode ",f.mode)
print("is file readable ", f.readable())
print("is file writable ", f.writable())
print("is file closed ", f.closed) # close the files otherwise you will get False 
f.close()
print("is file closed ", f.closed) # True 



# Writing data to text file 

f =open("bbc.txt","w")
f.write("hello this ")
f.write("is a file ")
f.write("i am wrtiting  ")
print("data written successfully")
f.close()

# check the file bbc.txt 

# in the above program data represents in the file will be overwritten 
# everytime if we run the program then go for append () a 

f=open("abc.txt","a")
f=open("abc.txt","w")
list = ["sunny\n","bunny\\n",'munny\n']
f.writelines(list)
print("data append siuccessfully to the file ")
f.close()

# TO read data from the files 

f=open("bbc.txt","r")
data = f.read()
print(data)
f.close ()

# to read only 10 character from the file 

f=open("abc.txt","r")
data = f.read(10)
print(data)
f.close ()


# TO read the data line by line 

f=open("abc.txt","r")
data =f.readline()
print("readline",data)
f.close()



# To read all the lines 

f=open("abc.txt","r")
data =f.readlines()

for d in data:
    print(d)
    f.close()


#example 

f=open("bbc.txt","r") 
data = f.read(4)
print(("four character",data)
data = f.readline()
print(data)
print("remianing data ")
print(f.read())  






































