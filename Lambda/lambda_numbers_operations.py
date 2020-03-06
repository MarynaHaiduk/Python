#!/usr/bin/python

if __name__ == "__main__":
    x = int(input("1st number: "))
    y = int(input("2nd number: "))

    sum_numbers = lambda x, y: x + y
    print("Sum:", sum_numbers(x, y))

    square_number = lambda x: x * x
    print("Square:", square_number(x))

    sum_elements = lambda nums: sum(nums)
    print("Sum of array elements:", sum_elements([1, 2, 3, 4, 5]))

    max_element = lambda nums: max(nums)
    print("Max in array:", max_element([1, 2, 3, 4, 5]))

    squares = list(map(lambda x: x**2, range(10)))
    squares = [x ** 2 for x in range(10)]  # same as above
