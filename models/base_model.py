#!/usr/bin/python3
"""
    This module contains the BaseModel
    that defines all common attributes/methods
    for other classes
"""
import models
import uuid
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
        This class will the base model
    """

    def __init__(self, *args, **kwargs):
        """
            It will initiate the object
        """
        if kwargs:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
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
        """
        Update the object
        The updated_at  iwth the current time
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        First piece of the serialization/deserialization process
        create dictionary representation of our class (BaseModel)
        """
        name = self.__class__.__name__
        New_dict = self.__dict__.copy()
        New_dict.update(__class__=name, created_at=self.created_at.isoformat())
        New_dict.update(updated_at=self.updated_at.isoformat())

        return New_dict
