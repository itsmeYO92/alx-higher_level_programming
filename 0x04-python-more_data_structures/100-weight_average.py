#!/usr/bin/python3
def weight_average(my_list=[]):
    _sum = 0
    coef = 0
    if my_list:
        for i in my_list:
            _sum += i[0] * i[1]
            coef += i[1]
    return _sum/coef
