#!/usr/bin/python3
"""create student class"""


class Student:
    """Defining class Student"""
    def __init__(self, first_name, last_name, age):
        """Initializing class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieve dictionary representation"""
        if (type(attrs)) == list and all(type(i) == str for i in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """update all the attributtes of class student"""
        for i in json:
            self.__dict__.update({i: json[i]})
