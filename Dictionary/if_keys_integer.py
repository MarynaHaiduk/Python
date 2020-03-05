def if_keys_integer(d):
    for k in d:
        if type(k) == int:
            return True
    return False

# Tests
print(if_keys_integer({"third": 3, "first": 1, "second": 2}))  # False
print(if_keys_integer({1: 3, 2: 4}))  # True
