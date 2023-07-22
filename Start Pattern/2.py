k = 1
n = int(input("enter numbers:"))
for i in range(1, n+1):
    for j in range(1,k+1):
        print("*", end='')
    k=k+2
    print()