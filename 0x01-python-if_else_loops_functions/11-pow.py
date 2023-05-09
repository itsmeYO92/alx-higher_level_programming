#!/usr/bin/python3
def pow(a, b):
    res = 1
    if b < 0:
        for i in range(-b):
            res = res / a
        return (res)
    for i in range(b):
        res = res * a
    return (res)
