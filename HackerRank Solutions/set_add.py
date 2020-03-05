#!/usr/bin/python

if __name__ == '__main__':
    country = set()
    i = 0
    number = int(input())
    while i < number:
        country.add(input())
        i += 1
    print(len(country))
