#!/usr/bin/python3
def uniq_add(my_list=[]):
    newList = []
    for x in my_list:
        if x not in newList:
            newList.append(x)
    return sum(newList)
