#!/usr/bin/python

def is_leap(year):
    leap = False
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        leap = True
    return leap

if __name__ == '__main__':
    year = int(input())
    print(is_leap(year))

# Tests
# Sample Input: 2018
# Sample Output: False
