from models.base_model import BaseModel
"""This module contains the User Class"""


class User(BaseModel):
    """The User Object"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
