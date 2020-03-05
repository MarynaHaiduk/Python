#!/usr/bin/python

import sys

if __name__ == '__main__':
    S = input().strip()
    try:
        print(int(S))
    except ValueError:
        print("Bad String")
