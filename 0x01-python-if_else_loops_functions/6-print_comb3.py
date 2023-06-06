#!/usr/bin/python3
for i in range(0, 10, 1):
    for v in range(0, 10):
        if i != v and i < v:
            print("{}{}".format(i, v), end='\n' if i == 8 and v == 9 else ', ')
