# Input:
# Str = HappyNewYear
# Output: HapyNewYr
def removeDuplicates(str):
    st=""
    for i in str:
            if(i not in st):
                st+=i
    return st
        
Str = "HappyNewYear"
print(removeDuplicates(Str))
