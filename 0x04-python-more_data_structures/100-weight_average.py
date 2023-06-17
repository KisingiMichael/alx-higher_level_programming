#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sumScore = 0
    sumWeight = 0
    for x in my_list:
        sumScore += x[0] * x[1]
        sumWeight += x[1]
    return sumScore / sumWeight
