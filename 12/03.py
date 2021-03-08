# Write  data to csv file 

import csv
with open("emp.csv" ,"w") as f :
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


# reading data from csv file 

import csv 
f = open("emp.csv" ,"r")
r =csv.reader(f)
data = list(r)
#print(data)
for line in data :
    for word in line :
        print(word ,"\t", end = "")
    print()
