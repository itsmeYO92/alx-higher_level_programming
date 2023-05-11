#!/usr/bin/python3
from sys import argv


def main():
    length = len(argv) - 1
    if length == 0:
        print("0 arguments.")
        return
    print("{:d} arguments:".format(length))
    for arg in argv[1:]:
        print("{:d}: {}".format(argv.index(arg), arg))


if __name__ == "__main__":
    main()
