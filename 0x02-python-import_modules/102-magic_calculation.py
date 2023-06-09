#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_102_caalculation import add, sub

    if a < b:
        m = add(a, b)
        for n in range(4, 6):
            m = add(m, n)
            return (m)
        else:
            return(sub(a, b))
    
