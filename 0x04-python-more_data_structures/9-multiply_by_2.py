#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}
    for keys, values in a_dictionary.items():
        new_dic[keys] = values * 2
    return (new_dic)
