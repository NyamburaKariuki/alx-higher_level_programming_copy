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

    def to_json(self):
        """retrieves a dictionary rep of student intsnace"""
        return self.__dict__
