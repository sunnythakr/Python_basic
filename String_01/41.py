def findSum(X, Y):
    # Convert the input strings to integers
    int_X = int(X)
    int_Y = int(Y)

    # Calculate the sum of the integers
    result = int_X + int_Y

    # Convert the sum back to a string and remove leading zeros
    result_str = str(result).lstrip('0')

    # Handle the case when the result is an empty string (due to all zeros being removed)
    if result_str == "":
        result_str = "0"

    return result_str

# Test cases
print(findSum("25", "23"))  # Output: "48"
print(findSum("2500", "23"))  # Output: "2523"