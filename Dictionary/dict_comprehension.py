def dict_comprehension(number):
    return {i: i*i for i in range(2, number)}

# Tests
print(dict_comprehension(6))  # {2: 4, 3: 9, 4: 16, 5: 25}
