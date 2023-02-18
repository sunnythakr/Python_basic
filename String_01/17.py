# Python Program that Displays which Letters are in First String but not in Second
def uncommon_letters(string1, string2):
    result = ""
    for letter in string1:
        if letter not in string2:
            result += letter
    for letter in string2:
        if letter not in string1:
            result += letter
    return result

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
print("Letters that are not common in both strings:", uncommon_letters(string1, string2))
