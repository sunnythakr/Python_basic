# frozenset is immutable you can not modify once you created that object 
s = {11,22,33,44,55}
f = frozenset(s)
for i in f:
    print(i)

print(type(f))
