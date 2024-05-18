#!/usr/bin/python3
"""Module creates a unique FileStorage instance for your application"""
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
from models.review import Review

storage = FileStorage()
storage.reload()
