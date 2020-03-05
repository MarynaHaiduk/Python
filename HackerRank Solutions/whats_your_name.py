#!/usr/bin/python

def print_full_name(first_name, last_name):
    return 'Hello {} {}! You just delved into Python.'.format(first_name, last_name)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    result = print_full_name(first_name, last_name)
    print(result)
