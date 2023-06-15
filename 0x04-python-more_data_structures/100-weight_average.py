#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    i = 0
    j = 0
    toto_weight = 0
    if my_list == 0:
        return 0
    else:
        for i, j in my_list:
            sum += (i * j)
            toto_weight += j
            j += 1
        if toto_weight == 0:
            return 0
        w = sum/toto_weight
        return w
