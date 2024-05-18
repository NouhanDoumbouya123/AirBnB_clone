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
        if args == 0:
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
        created = self.created_at.isoformat()
        updated = self.updated_at.isoformat()
        json_obj = self.__dict__.copy()
        json_obj.update({"__class__": __class__.__name__,
                         "updated_at": updated,
                         "created_at": created})
        return json_obj
