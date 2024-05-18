#!/usr/bin/python3
"""
    This module contains the BaseModel
    that defines all common attributes/methods
    for other classes
"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """
    This class will be the base model
    """

    def __init__(self, *args, **kwargs):
        """It will initiate the object"""
        if kwargs:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                elif k == 'updated_at' or k == 'created_at':
                    self.__setattr__(k, datetime.datetime.fromisoformat(v))
                self.__setattr__(k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """Returns the string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the object
        The updated_at  iwth the current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        First piece of the serialization/deserialization process
        create dictionary representation of our class (BaseModel)
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
