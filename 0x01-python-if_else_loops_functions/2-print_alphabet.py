#!/usr/bin/python3
delim = ""
for i in range(97, 123):
    if i == 122:
        delim = "\n"
    print(chr(i), end=delim)
