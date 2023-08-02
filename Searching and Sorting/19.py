# Given an integer x, find the square root of x. 
# If x is not a perfect square, then return floor(√x).
# Input:
# x = 5
# Output: 2
# Explanation: Since, 5 is not a perfect 
# square, floor of square_root of 5 is 2.
def floorSqrt(x): 
    #Your code here
        if x == 0 or x == 1:
            return x

        left, right = 1, x
        result = 0

        while left <= right:
            mid = (left + right) // 2

            # If the square of mid is less than or equal to x, update the result and search in the right half
            if mid * mid <= x:
                result = mid
                left = mid + 1
            else:  # If the square of mid is greater than x, search in the left half
                right = mid - 1

        return result