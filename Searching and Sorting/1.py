# search the element in an array 
def arrsearch(arr,N,K):
    for i in range(0, N):
        if arr[i] ==K:
            return 1
    return -1

arr  =[1,3,4,6]
N =len(arr)
K = 2
print(arrsearch(arr, N, K))