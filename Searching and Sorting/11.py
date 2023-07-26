def two(arr,n):
    # lst1 = []
    # rpt = []
    # for i in range(0,n):
    #     if arr[i] in lst1:
    #         rpt.append(arr[i])
    #     else:
    #         lst1.append(arr[i])
    # return rpt
    s=set()
    res=[]
    for i in arr:
        if i not in s:
            s.add(i)
        else:
            res.append(i)
    return res#Your code here

# example 1
arr = [1,2,1,3,4,3]
n = len(arr)
print(two(arr,n))

# example 2
arr1 = [1,2,2,1]
n = len(arr1)
print(two(arr1,n))

