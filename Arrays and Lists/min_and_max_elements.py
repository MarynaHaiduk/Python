def min_and_max_elements(arr):
    min_el = max_el = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_el:
            max_el = arr[i]
        if arr[i] < min_el:
            min_el = arr[i]
    return min_el, max_el

# Tests
print(min_and_max_elements([77, 1, 2, 44, 5]))  # (1, 77)
