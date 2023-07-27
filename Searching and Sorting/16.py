# Given two arrays of length N and M, print the merged array in ascending 
# order containing only unique elements.
def sorttwoarray(a,b,n,m):
    merge_ab = a + b
    answer = []
    for i in merge_ab:
        if i not in answer:
            answer.append(i)
    answer.sort()
    answer_len = len(answer)
    return answer_len

a = [7, 1, 5, 3, 9]
b = [8, 4, 3, 5, 2, 6]
# a = [1,8]
# b = [10,11]
n = len(a)
m = len(b)

print(sorttwoarray(a,b,m,n))
