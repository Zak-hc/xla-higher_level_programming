#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_lista = my_list.copy()
    my_lista[my_list.index(search)] = replace
    return my_lista
