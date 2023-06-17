#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or roman_string is None):
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    new_list = 0
    for x in range(len(roman_string)):
        if roman.get(roman_string[x], 0) == 0:
            return 0

        if (x != (len(roman_string) -1) and roman[roman_string[x]] < roman[roman_string[x + 1]]):
            new_list += roman[roman_string[x]] * -1
        else:
            new_list += roman[roman_string[x]]
        return new_list
