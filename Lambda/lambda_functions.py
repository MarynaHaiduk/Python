func = lambda x, y: x + y
print(func(1, 2))  # 3
print(func('a', 'b'))  # 'ab'

# the same as above
print((lambda x, y: x + y)(1, 2))  # 3
print((lambda x, y: x + y)('a', 'b'))  # 'ab'
print((lambda x, y: x + y).__call__('a', 'b'))  # 'ab'

func = lambda *args: args
print(func(1, 2, 3, 4))  # (1, 2, 3, 4)
func = lambda *args: args[0]
print(func(1, 2, 3, 4))  # 1

def sum(b):
    return lambda a: a + b
result = sum(2)
print(result(5))
