#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1

    if argc == 0:
        print("{} arguments.".format(argc))
    elif argc == 1:
        print("{} argument:".format(argc))
    else:
        print("{} arguments:".format(argc))

    if argc >= 1:
        argc = 0
        for n in sys.argv:
            if argc != 0:
                print("{}: {}".format(argc, n))
            argc += 1
