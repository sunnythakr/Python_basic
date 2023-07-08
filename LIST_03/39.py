# rearrange array 
def rearrange(arr, n):
    max_idx = n - 1
    min_idx = 0
    max_element = arr[max_idx] + 1

    for i in range(n):
        if i % 2 == 0:
            arr[i] += (arr[max_idx] % max_element) * max_element
            max_idx -= 1
        else:
            arr[i] += (arr[min_idx] % max_element) * max_element
            min_idx += 1

    for i in range(n):
        arr[i] = arr[i] // max_element

    # The modified array is updated in-place, so there is no need to return it

# Example usage:
n = 6
arr = [1, 2, 3, 4, 5, 6]
rearrange(arr, n)
print(arr)  # Output: [6, 1, 5, 2, 4, 3]