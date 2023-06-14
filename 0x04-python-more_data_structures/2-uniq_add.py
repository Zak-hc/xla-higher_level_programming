#!/usr/bin/python3
def uniq_add(my_list=[]):
    compa = list(set(my_list))
    resultat = 0
    for i in range(len(compa)):
        resultat += compa[i]
    return resultat
