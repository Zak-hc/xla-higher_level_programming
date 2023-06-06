#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            v = chr(ord(i) - 32)
            print("{:s}".format(v), end="")
    print()
