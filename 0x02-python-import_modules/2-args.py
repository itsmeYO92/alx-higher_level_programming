#!/usr/bin/python3
from sys import argv


def main():
    length = len(argv) - 1
    if length == 0:
        print("0 arguments.")
        return
    if length == 1:
        print("{:d} argument:".format(length))
    else:
        print("{:d} arguments:".format(length))
    for arg in argv[1:]:
        print("{:d}: {}".format(argv.index(arg), arg))


if __name__ == "__main__":
    main()
