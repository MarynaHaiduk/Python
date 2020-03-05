#!/usr/bin/python

def mutate_string(string, pos, char):
    new_string = string[0:pos] + char + string[pos+1:]
    return new_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
