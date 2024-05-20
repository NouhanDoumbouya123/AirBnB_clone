"""
Contains the TestFileStorageDocs classes
"""

import json
import inspect
import pycodestyle
import unittest
import sys
import os

# Get the absolute path of the parent
# directory (two levels up from the current file)
parent_dir = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '../..'))

# Insert the parent directory path at the beginning of the sys.path list
sys.path.insert(0, parent_dir)

file_storage = __import__("models").engine.file_storage
FileStorage = file_storage.FileStorage
BaseModel = __import__("models").base_model.BaseModel
User = __import__("models").user.User
Amenity = __import__("models").amenity.Amenity
City = __import__("models").city.City
Place = __import__("models").place.Place
Review = __import__("models").review.Review
State = __import__("models").state.State


class TestFileStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of FileStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.file_storage_f = inspect.getmembers(
            FileStorage, inspect.isfunction)

    def test_pycodestyle_conformance_file_storage(self):
        """Test that models/engine/file_storage.py conforms to pycodestyle."""
        pycodestyles = pycodestyle.StyleGuide(quiet=True)
        result = pycodestyles.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_file_storage_module_docstring(self):
        """Test for the file_storage.py module docstring"""
        self.assertIsNot(file_storage.__doc__, None,
                         "file_storage.py needs a docstring")
        self.assertTrue(len(file_storage.__doc__) >= 1,
                        "file_storage.py needs a docstring")

    def test_file_storage_class_docstring(self):
        """Test for the FileStorage class docstring"""
        self.assertIsNot(FileStorage.__doc__, None,
                         "FileStorage class needs a docstring")
        self.assertTrue(len(FileStorage.__doc__) >= 1,
                        "FileStorage class needs a docstring")

    def test_file_storage_func_docstrings(self):
        """Test for the presence of docstrings in FileStorage methods"""
        for func in self.file_storage_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    def test_all(self):
        """Test the all method"""
        fs = FileStorage()
        all_objs = fs.all()
        self.assertEqual(type(all_objs), dict)
        self.assertIs(all_objs, fs._FileStorage__objects)

    def test_new(self):
        """Test the new method"""
        fs = FileStorage()
        obj = BaseModel()
        fs.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertIn(key, fs.all().keys())

    def test_save(self):
        """Test the save method"""
        fs = FileStorage()
        obj = BaseModel()
        fs.new(obj)
        fs.save()
        with open(fs._FileStorage__file_path, 'r') as file:
            saved_data = json.load(file)
        self.assertIn("BaseModel." + obj.id, saved_data)

    def test_reload(self):
        """Test the reload method"""
        fs = FileStorage()
        obj = BaseModel()
        fs.new(obj)
        fs.save()
        fs.reload()
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertIn(key, fs.all().keys())


if __name__ == "__main__":
    unittest.main()
