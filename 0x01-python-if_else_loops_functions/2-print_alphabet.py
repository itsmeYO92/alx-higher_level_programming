#!/usr/bin/python3
delim = ""
for i in range(97, 123):
    if i == 122:
        delim = "\n"
    print("{}".format(chr(i)), end=delim)
