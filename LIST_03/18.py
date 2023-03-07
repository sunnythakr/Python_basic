# Reversing a List in Python
lst = [1,2,3,4,5]
rev_lst = []
counter = 0
for i in range(len(lst),0,-1):
    rev_lst.append(i)
print(rev_lst)