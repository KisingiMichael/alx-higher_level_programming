#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv)
    summation = 0

    for n in range(i - 1):
        summation += int(sys.argv[n + 1])
    print("{}".format(summation))
