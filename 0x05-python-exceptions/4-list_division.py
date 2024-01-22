#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    '''divides element by element 2 lists
    Returns a new list (length = list_length) with all divisions
    If an element is not an integer or float:
        print: wrong type
    If the division can’t be done (/0):
        print: division by 0
    If my_list_1 or my_list_2 is too short
        print: out of range'''

    new_list = []
    for item in range(list_length):
        try:
            result = my_list_1[item] / my_list_2[item]
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        finally:
            new_list.append(result)
    return new_list
