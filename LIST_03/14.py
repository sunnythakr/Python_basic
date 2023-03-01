# s = "my name is python"
# l = s.split()
# l1 = []
# i = 0
# while i < len(l):
#     print(l[i])
#     l1.append(l[i][::-1])
#     i = i+1
# output = "".join(l1)
# print(l1)
num = 7
for col in range(0, num):
    for row in range(0,(num//2)+1):
        print("*", end =" ")
    print()