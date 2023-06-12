#!/usr/bin/python3
""" MyList module inherent from List """


class MyList(list):
    """ MyList class - inherent from list  """

    def print_sorted(self):
        """ print a sorted list """
        print(sorted(self))
