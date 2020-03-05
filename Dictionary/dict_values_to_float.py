def dict_values_to_float(d):
    for k, v in d.items():
        d[k] = float(v)
    return d

# Tests
print(dict_values_to_float({"a": 1, "b": 2, "c": 7}))
