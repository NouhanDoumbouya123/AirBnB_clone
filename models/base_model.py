#!/usr/bin/python3
"""
    This module contains the BaseModel
    that defines all common attributes/methods
    for other classes
"""
import uuid
import datetime


class BaseModel:
    """this class will be the base model"""
    id = str(uuid.uuid4())
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    def __init__(self) -> None:
        """It will initiate the object"""
        self.id = __class__.id
        self.created_at = __class__.created_at
        self.updated_at = __class__.updated_at

    def __str__(self):
        """returns the string representation"""
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update the object"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        First piece of the serialization/deserialization process
        create dictionary representation of our class (BaseModel)
        """
        created = self.created_at.isoformat()
        updated = self.updated_at.isoformat()
        json_obj = self.__dict__
        json_obj.update({"__class__": __class__.__name__,
                         "updated_at": updated,
                         "created_at": created})
        return json_obj
