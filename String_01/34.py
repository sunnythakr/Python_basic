# Input:
# S = i.like.this.program.very.much
# Output: much.very.program.this.like.i
def reverseWords(S):
        words = []
        split_words =S.split('.')
        for i in range(len(split_words)-1,-1,-1):
            words.append(split_words[i])
        
        join_words = '.'.join(words)
        return join_words

str = "i.like.this.program.very.much"
print(reverseWords(str))