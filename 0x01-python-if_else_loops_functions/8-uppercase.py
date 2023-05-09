#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        if 96 < ord(i) < 123:
            i = chr(ord(i) - 32)
            result = result + i
        else:
            result = result + i
    print("{}".format(result))
