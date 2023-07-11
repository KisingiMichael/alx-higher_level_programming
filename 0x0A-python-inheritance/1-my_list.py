#!/usr/bin/python3
""" Creating MyList class """


class MyList(list):
    """
    MyList inherits from class list
    """
    def print_sorted(self):
        """
        prints the list in sorted order
        """
        print(sorted(self))
