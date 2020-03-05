def count_camelcase_chars(s):
    count = 0
    for i in s:
        if i.isupper():
            count += 1
    return count

# Tests
print(count_camelcase_chars('ckjkUUYII'))  # 5
print(count_camelcase_chars('HKJT'))  # 4
print(count_camelcase_chars('njnnk'))  # 0
