#!/usr/bin/python3
import dis
def magic_calculation(a, b, c):
    if a < b:
        if c > b:
            return ((a * b) - c)
        else:
            return (a + b)
    else:
        return (c)

dis.dis(magic_calculation)
