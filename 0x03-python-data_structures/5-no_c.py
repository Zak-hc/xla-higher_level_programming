#!/usr/bin/python3
def no_c(my_string):
    for idx in my_string:
        if idx != 'c' and idx != 'C':
            print("{}".format(idx), end='')
