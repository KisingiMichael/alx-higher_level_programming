#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newList = []
    for n in range(0, list_length):
        try:
            num = my_list_1[n] / my_list_2[n]
        except TypeError:
            print("wrong type")
            num = 0
        except ZeroDivisionError:
            print("division by 0")
            num = 0
        except IndexError:
            print("out of range")
            num = 0
        finally:
            newList.append(num)
    return (newList)
