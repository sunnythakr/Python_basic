# Given an unsorted array Arr of N positive and negative numbers. Your task is to create an array of alternate positive and negative numbers without changing the relative order of positive and negative numbers.
# Note: Array should start with a positive number.
class Solution:
    def rearrange(self, arr, n):
        positive = []
        negative = []
        
        # Separate positive and negative numbers
        for num in arr:
            if num >= 0:
                positive.append(num)
            else:
                negative.append(num)
        
        result = []
        p_idx = 0
        n_idx = 0
        
        # Merge positive and negative numbers alternately
        while p_idx < len(positive) and n_idx < len(negative):
            result.append(positive[p_idx])
            result.append(negative[n_idx])
            p_idx += 1
            n_idx += 1
        
        # Append remaining positive or negative numbers
        while p_idx < len(positive):
            result.append(positive[p_idx])
            p_idx += 1
        
        while n_idx < len(negative):
            result.append(negative[n_idx])
            n_idx += 1
        
        # Update the original array
        for i in range(n):
            arr[i] = result[i]

