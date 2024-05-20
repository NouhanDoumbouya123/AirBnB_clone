#!/usr/bin/python3
from models.base_model import BaseModel
"""This module contains the Review Class"""


class Review(BaseModel):
    """The attributes of the class"""
    place_id = ""
    user_id = ""
    text = ""
