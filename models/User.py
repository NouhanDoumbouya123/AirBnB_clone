#!/usr/bin/python3
"""This modul contains the User Class"""
from .base_model import BaseModel

class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
