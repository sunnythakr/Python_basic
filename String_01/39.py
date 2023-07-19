# Input:
# Str = HappyNewYear
# Output: HapyNewYr
def removeDuplicates(str):
    seen = set()  # Set to keep track of encountered characters
    result = ""  # Resultant string

    for char in str:
        if char.lower() not in seen:
            seen.add(char.lower())
            result += char

    return result
Str = "HappyNewYear"
print(removeDuplicates(Str))
