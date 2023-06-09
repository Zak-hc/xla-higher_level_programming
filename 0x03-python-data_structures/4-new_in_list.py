#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a = my_list.copy()
    b = int(idx)
    c = my_list.copy()
    if 0 <= b < len(c):
        c[idx] = element
        return c
        return a
    elif b < 0 or b >= len(a):
        return a
