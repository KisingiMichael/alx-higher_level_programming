#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cnt = 0
    for n in range(x):
        try:
            print("{:d}".format(my_list[n]), end="")
            cnt += 1
            for x in range(cnt):
                print("", end="")
        except (TypeError, ValueError):
            print("", end="")
    print()
    return (cnt)
