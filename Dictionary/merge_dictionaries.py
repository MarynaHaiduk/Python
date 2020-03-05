# Solution 1
def merge_dictionaries1(d1, d2):
    merged = {}
    merged.update(d1)
    merged.update(d2)
    return merged

# Solution 2
def merge_dictionaries2(d1, d2):
    merged = {**d1, **d2}
    return merged

# Tests
d1 = {'a': 10, 'b': 8}
d2 = {'d': 6, 'c': 4}
print(merge_dictionaries1(d1, d2))  # {'a': 10, 'b': 8, 'd': 6, 'c': 4}
print(merge_dictionaries2(d1, d2))  # {'a': 10, 'b': 8, 'd': 6, 'c': 4}
