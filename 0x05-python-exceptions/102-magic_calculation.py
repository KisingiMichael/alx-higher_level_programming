#!/usr/bin/python3
def magic_calculation(a, b):
    results = 0
    for n in range(1, 3):
        try:
            if n > a:
                raise Exception("Too far")
            else:
                results += (a ** b) / n
        except Exception:
            results = b + a
            break
    return results
