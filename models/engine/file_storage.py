#!/usr/bin/python3
"""
This module include the FileStorage
"""
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import json
import os

class FileStorage:
    """
    Serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with
        the id of class as a key
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes objects to the JSON file
        """

        # read existing data
        existing_data = {}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                existing_data = json.load(file)

        # update the data with the new objects
        new_data = {key: obj.to_dict() for key, obj in self.__objects.items() if isinstance(obj, BaseModel)}

        existing_data.update(new_data)

        # write it to the file
        with open(self.__file_path, "w") as file:
            json.dump(existing_data, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        if os.path.exists(self.__file_path) and\
                os.path.getsize(self.__file_path) > 0:
            with open(self.__file_path, "r") as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    cls_name = value['__class__']
                    cls = globals().get(cls_name)
                    self.__objects[key] = cls(**value)
