# Reverse words in a given String in Python
st = "sunny is name my"
s=  st.split()[::-1]
l = []
for i in s:
    l.append(i)
print(l)
print(" ".join(l))
