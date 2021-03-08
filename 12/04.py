# Zipping and unzipping FIles 

# The main advantages are 
# 1. to improve memory utilization 
# 2. we can reduce transport time 
# 3. We can improve performance 

# TO create zip file \
# f= ZipFile("files.zip","w","ZIP_DEFLATED")

# Once we create ZipFile object can be add files by using write() method 

from zipfile import*
f=ZipFile("files.zip",'w',ZIP_DEFLATED)
f.write("abc.txt")
f.write("acc.txt")
f.write("bbc.txt")
f.close()
print('files.zip file created successfully')



# TO perform unzip Operations 

# f= ZipFile("files.zip","r",ZIP_STORED) # ZIP_STORED represent the unzip operations 

from zipfile import*
f= ZipFile("files.zip","r",ZIP_STORED)
names = f.namelist()
for name in names:
    print("file name", name)
    print("the content of this file ")
    f1=open(names,'r')
    print(f1.read())
    print()