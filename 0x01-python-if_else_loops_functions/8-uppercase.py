#!/usr/bin/python3
def uppercase(str):
    for wd in str:
        if (ord(wd) > 96 and ord(wd) <= 124):
            wd = chr(ord(wd) - 32)
        print("{}".format(wd), end='')
    print()
