#!/usr/bin/python3
"""
    This module contains the BaseModel
    that defines all common attributes/methods
    for other classes
"""
from models import storage
import uuid
import datetime


class BaseModel:
    """this class will be the base model"""
    id = str(uuid.uuid4())
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    def __init__(self, *args, **kwargs):
        """It will initiate the object"""
        self.id = __class__.id
        self.created_at = __class__.created_at
        self.updated_at = __class__.updated_at
        storage.new(self)
        if args == 0:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                elif k == 'updated_at' or k == 'created_at':
                    self.__setattr__(k, datetime.datetime.fromisoformat(v))
                self.__setattr__(k, v)

    def __str__(self):
        """returns the string representation"""
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update the object"""
        self.updated_at = datetime.datetime.now()
        storage.save()

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
