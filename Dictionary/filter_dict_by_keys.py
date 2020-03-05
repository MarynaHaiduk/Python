# Solution 1
# def filter_dict_by_key(d, number):
#     res = {}
#     for key, value in d.items():
#         if key <= number:
#             res[key] = value
#     return res

# Solution 2
def filter_dict_by_key(d, number):
    return {i:d[i] for i in d if i <= number}

# Test
d = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
print(filter_dict_by_key(d, 2))  # {1: 'a', 2: 'b'}
