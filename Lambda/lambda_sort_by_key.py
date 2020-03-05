def sort_by_key(arr):
    arr.sort(key=lambda pair: pair[1])
    return arr

# Tests
arr = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
print(sort_by_key(arr))  # [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
