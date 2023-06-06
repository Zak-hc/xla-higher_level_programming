#!/usr/bin/python3
for z in range(0, 100, 1):
    print("{:02d}".format(z), end=', 'if z < 99 else '\n')
