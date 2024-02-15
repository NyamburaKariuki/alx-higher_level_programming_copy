#!/usr/bin/python3
"""module contain the base class, its attributes and methods"""
import json
import turtle
import csv


class Base:
    """base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """instancitaion of a class'''
        args: Id(integer)"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = "{}.json".format(cls.__name__)
        list_d = []
        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_d.append(list_objs[i].to_dictionary())
        list_s = cls.to_json_string(list_d)
        with open(filename, 'w') as file:
            file.write(list_s)

    @staticmethod
    def from_json_string(json_string):
        """eturns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "[]":
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, 'r') as f:
                lists = Base.from_json_string(f.read())
                return [cls.create(**dicts) for dicts in lists]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fields=fields)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Returns:
            An empty list- if the file does not exit
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                list_d = csv.DictReader(f, fields=fields)
                list_d = [
                    dict([k, int(v)] for k, v in dc.items()) for dc in list_d
                ]
                return [cls.create(**dc) for dc in list_d]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turtle_t = turtle.Turtle()
        turtle_t.screen.bgcolor("#b7312c")
        turtle_t.pensize(5)
        turtle_t.shape("turtle")

        turtle_t.color("yellow")
        for rectangle in list_rectangles:
            turtle_t.showturtle()
            turtle_t.up()
            turtle_t.goto(rectangle.x, rectangle.y)
            turtle_t.down()
            for x in range(2):
                turtle_t.forward(rectangle.width)
                turtle_t.left(90)
                turtle_t.forward(rectangle.height)
                turtle_t.left(90)
            turtle_t.hideturtle()

        turtle_t.color("blue")
        for square in list_squares:
            turtle_t.showturtle()
            turtle_t.up()
            turtle_t.goto(square.x, square.y)
            turtle_t.down()
            for x in range(2):
                turtle_t.forward(square.width)
                turtle_t.left(90)
                turtle_t.forward(square.height)
                turtle_t.left(90)
            turtle_t.hideturtle()

        turtle.exitonclick()
