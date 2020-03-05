# Solution 1 (save the order)
def remove_duplicates(arr):
    res = []
    for i in arr:
        if i not in res:
            res.append(i)
    return res

# Solution 2 (fast, don't save the order)
# def remove_duplicates(arr):
#     return list(set(arr))

# Tests
print(remove_duplicates([1, 4, 2, 3, 3, 4, 1]))  # [1, 4, 2, 3]
