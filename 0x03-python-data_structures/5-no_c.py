#!/usr/bin/python3
def no_c(my_string):
    a = ""
    for idx in my_string:
        if idx != 'c' and idx != 'C':
            a += idx
    return a
