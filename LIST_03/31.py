# Given an array of penalties fine[],
#  an array of car numbers car[], and also 
# the date. The task is to find the total fine
#  which will be collected on the given date. Fine is 
# collected from odd-numbered cars on even dates and vice versa.

# Input:
# N = 4, date = 12
# car[] = {2375, 7682, 2325, 2352}
# fine[] = {250, 500, 350, 200}
# Output:
# 600
# Explantion:
# The date is 12 (even), so we collect the
# fine from odd numbered cars. The odd
# numbered cars and the fines associated
# with them are as follows:
# 2375 -> 250
# 2325 -> 350
# The sum of the fines is 250+350 = 600

class Solution:
    def totalFine(self, n, date, car, fine):
        #Code here
        total_fine = 0
        for i in range(n):
            if date%2 == 0 and car[i]%2 != 0: # even date, odd numbered car
                total_fine += fine[i]
            elif date%2 != 0 and car[i]%2 == 0: # odd date, even numbered car
                total_fine += fine[i]
        return total_fine

S = Solution()
N = 4
date = 12
car = [2375, 7682, 2325, 2352]
fine = [250, 500, 350, 200]
print(S.totalFine(N, date, car, fine)) 