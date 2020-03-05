def remove_numeric_digits(s):
    res = ""
    for i in s:
        if not i.isdigit():
            res += i
    return res

# Tests
print(remove_numeric_digits("akshat123garg"))  # akshatgarg
