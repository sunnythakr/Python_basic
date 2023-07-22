# #example one 
def summation(n):
    sum = 0
    for i in range(n+1):
        sum +=i
    return sum
    return n *(n+1)//2

n =  int(input("enter numer"))
print(summation(n))

# # Example 2
def summation(n):
    return n *(n+1)//2

n =  int(input("enter numer"))
print(summation(n))

#example 3

def summation(n):
    sum = 0
    for i in range(0,n+1):
        for j in range(0,i):
            sum +=1
    return sum

n =  int(input("enter numer"))
print(summation(n))