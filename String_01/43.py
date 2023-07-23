def removeReverse(S):
    stack = []
    seen = set()

    for char in S:
        if char not in seen:
            stack.append(char)
            seen.add(char)
        else:
            # Removing the first occurrence of the repeating character
            while stack and stack[-1] != char:
                seen.remove(stack.pop())

    return "".join(stack[::-1])

# Example 1
S1 = "abab"
print(removeReverse(S1))  # Output: "ba"

# Example 2
S2 = "dddd"
print(removeReverse(S2))  # Output: "d"
