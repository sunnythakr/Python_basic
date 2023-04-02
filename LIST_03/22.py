n  = int(input("Enter the number: "))
lst = []
for r in range(1,n+1):
    num = int(input("enter the num: "))
    lst.append(num)
l =  len(lst)
def  interchange(lst):
        lst[0],lst[l-1] = lst[l-1], lst[0]
        return lst

# interchange(lst)
print("List is:", lst)
print(interchange(lst))

