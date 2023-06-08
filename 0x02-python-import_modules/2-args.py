#!/usr/bin/python3
import sys
if __name__ == '__main__':
    a = sys.argv
    z = len(a) - 1
    if z == 0:
        print("{} arguments.".format(z))
    elif z == 1:
        print("{} arguments:".format(z))
        print("{}: {}".format(z, a[1]))
    else:
        print("{} arguments:".format(z))
        for n in range(1, len(a)):
            print("{}: {}".format(n, a[n]))
