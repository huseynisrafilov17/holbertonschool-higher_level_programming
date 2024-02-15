#!/usr/bin/python3
'''
My module
'''
import json


class Base:
    '''
    Base Class
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        save_to_file writes the JSON string of list_objs to a file
        Args:
            list_objs: object list
        '''
        c_n = cls.__name__
        if list_objs is None:
            with open("{}.json".format(c_n), "w", encoding="utf-8") as f:
                f.write("[]")
        else:
            li = []
            for i in list_objs:
                li.append(i.to_dictionary())
            with open("{}.json".format(c_n), "w", encoding="utf-8") as f:
                f.write(cls.to_json_string(li))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        else:
            return json.loads(json_string)
