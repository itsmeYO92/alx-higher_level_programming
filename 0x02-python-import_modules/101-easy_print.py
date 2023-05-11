#!/usr/bin/python3
import os


def main():
    a = "#pythoniscool\n"
    os.write(1, a.encode())


if __name__ == "__main__":
    main()
