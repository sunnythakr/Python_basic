def floor(arr, n,x):
    i =0
    while(n>0):
        if arr[i] < x:
            return 1
            i +=1
        return -1
arr = [1,2,8,10,11,12,19]
n = len(arr)
x = 5
print(floor(arr,n,x))