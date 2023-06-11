#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    a = int(idx)
    b = my_list
    c = int(element)
    if 0 <= a < len(b):
        b[a] = element
        return(b)
    elif a < 0 or a >= len(b):
        return(b)
