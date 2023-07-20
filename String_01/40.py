def minFlips(S):
    def count_flips(start_char, s):
        flips = 0
        for char in s:
            if char != start_char:
                flips += 1
            start_char = '1' if start_char == '0' else '0'
        return flips
    
    return min(count_flips('0', S), count_flips('1', S))

s  ="0001010111"
print(minFlips(s))