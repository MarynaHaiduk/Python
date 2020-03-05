def sum_of_cubes(number):
    cubes = [i ** 3 for i in range(1, number+1)]
    return sum(cubes)

# Tests
print(sum_of_cubes(10))  # 3025
