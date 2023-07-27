def orderedSort(arr,n):

    # odd = []
    # even = []
    # for i in arr:
    #     if (i%2!=0):
    #         odd.append(i)
    #     else:
    #         even.append(i)
    
    # seperate odd even element 
    odd = [x for x in arr if x%2 != 0]
    even = [x for x in arr if x%2 == 0]

    odd.sort(reverse=True)
    even.sort()
    arr[:len(odd)] = odd
    arr[len(even):] = even
    return arr

    # return odd + even

# arr  =[1, 2, 3, 5, 4, 7, 10]
arr = [0, 4, 5, 3, 7, 2, 1]
n = len(arr)
print(orderedSort(arr,n))
