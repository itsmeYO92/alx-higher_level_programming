#!/usr/bin/python3
""" stats module to parse logs """


import sys


stats = {"200": 0, "301": 0, "400": 0, "401": 0,
         "403": 0, "404": 0, "405": 0, "500": 0}
size = 0
line_count = 1


def print_stats(stats={}):
    print("File size: {}".format(size))
    for key, value in stats.items():
        print("{}: {}".format(key, value))


try:
    for line in sys.stdin:
        splited_line = line.split(" ")
        size += int(splited_line[-1])
        stats[splited_line[-2]] += 1
        line_count += 1
        if line_count == 10:
            print_stats(stats)
            line_count = 1
except KeyboardInterrupt:
    print_stats(stats)
