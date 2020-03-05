#!/usr/bin/python

if __name__ == '__main__':
    num1 = input('1st number: ')
    num2 = input('2nd number: ')
    try:
        first = float(num1)
        second = float(num2)
        quotient = first / second
        print('Quotient 1st/2nd = ', quotient)
    except Exception as diag:
        # diag.__class__.__name__ returns names the error type
        print(diag.__class__.__name__, ':', diag)
