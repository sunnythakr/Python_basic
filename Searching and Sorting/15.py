def sort(s): 
        lst = [s[i] for i in range(0,len(s))]
        lst.sort()
        str_sum = ''
        for i in lst:
            str_sum +=i
        return str_sum

# Example
s = 'edcab'
print(sort(s))