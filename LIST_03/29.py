# def segregateElements(arr, n):
        # My solution
        # pos = []
        # neg = []
        # for i in arr:
        #     if i < 0:
        #         neg.append(i)
        #     else:
        #         pos.append(i)
        # print(pos)
        # return pos + neg

#User function Template for python3

class Solution:
    def segregateElements(self, arr, n):
        # Your code goes here
        arr1 = []
        for i in arr:
            if i>0:
                arr1.append(i)
                
        for j in arr:
            if j<0:
                arr1.append(j)
                
        for k in range(n):
            arr[k] = arr1[k]
        
        return arr