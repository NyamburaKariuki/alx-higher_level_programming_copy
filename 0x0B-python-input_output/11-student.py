#!/usr/bin/python3
"""module with class student"""


class Student:
    """defines property of a student
    Attributes:
    first_name(str): student's first name
    last_name(str): student's last name
    age: students age"""
    def __init__(self, first_name, last_name, age):
        """creates a new instance of a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary rep of student intsnace"""
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
