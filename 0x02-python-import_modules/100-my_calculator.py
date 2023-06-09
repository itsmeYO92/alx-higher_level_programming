#!/usr/bin/python3
import calculator_1 as calc
from sys import argv


def main():
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if argv[2] == '+':
        print("{:d} {} {:d} = {:d}".format(a, argv[2], b, calc.add(a, b)))
    elif argv[2] == '-':
        print("{:d} {} {:d} = {:d}".format(a, argv[2], b, calc.sub(a, b)))
    elif argv[2] == '*':
        print("{:d} {} {:d} = {:d}".format(a, argv[2], b, calc.mul(a, b)))
    elif argv[2] == '/':
        print("{:d} {} {:d} = {:d}".format(a, argv[2], b, calc.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    main()
