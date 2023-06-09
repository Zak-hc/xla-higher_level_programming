#!/usr/bin/python3
def element_at(my_list, idx):
    pip = int(idx)
    if 0 <= pip < len(my_list):
        return(my_list[idx])
    elif pip < 0 or pip >= len(my_list):
        return None
