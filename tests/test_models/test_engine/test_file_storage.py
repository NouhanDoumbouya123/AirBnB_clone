#!/usr/bin/python3
"""Test FileStorage for expected behavior and documentation"""
import unittest
import os
import sys
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../..')))
FileStorage = __import__('models.engine.file_storage').FileStorage



