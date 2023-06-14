#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_lista = my_list.copy()
    for idx in range(len(my_lista)):
        if my_lista[idx] == search:
            my_lista[idx] = replace
    return my_lista
