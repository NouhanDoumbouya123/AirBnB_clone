#!/usr/bin/python3
"""
Contains the TestBaseModelDocs classes
"""

from datetime import datetime
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

base_model = __import__("models").base_model
BaseModel = base_model.BaseModel


class TestBaseModelDocs(unittest.TestCase):
    """Tests to check the documentation and style of BaseModel class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.base_model_f = inspect.getmembers(
            BaseModel, inspect.isfunction)

    def test_pycodestyle_conformance_base_model(self):
        """Test that models/base_model.py conforms to pycodestyle."""
        pycodestyles = pycodestyle.StyleGuide(quiet=True)
        result = pycodestyles.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_base_model_module_docstring(self):
        """Test for the base_model.py module docstring"""
        self.assertIsNot(base_model.__doc__, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(base_model.__doc__) >= 1,
                        "base_model.py needs a docstring")

    def test_base_model_class_docstring(self):
        """Test for the BaseModel class docstring"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")

    def test_base_model_func_docstrings(self):
        """Test for the presence of docstrings in BaseModel methods"""
        for func in self.base_model_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""
    def test_id_attr(self):
        """Test that BaseModel has attribute id, and it's a string"""
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, "id"))
        self.assertIsInstance(base_model.id, str)

    def test_created_at_attr(self):
        """Test that BaseModel has attribute created_at, and it's a datetime"""
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, "created_at"))
        self.assertIsInstance(base_model.created_at, datetime)

    def test_updated_at_attr(self):
        """Test that BaseModel has attribute updated_at, and it's a datetime"""
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, "updated_at"))
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_str(self):
        """Test that the str method has the correct output"""
        base_model = BaseModel()
        string = "[BaseModel] ({}) {}".format(
            base_model.id, base_model.__dict__)
        self.assertEqual(string, str(base_model))

    def test_save_updates_updated_at(self):
        """Test that save method updates the updated_at attribute"""
        base_model = BaseModel()
        old_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(old_updated_at, base_model.updated_at)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        b = BaseModel()
        new_d = b.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in b.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        b = BaseModel()
        new_d = b.to_dict()
        self.assertEqual(new_d["__class__"], "BaseModel")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"],
                         b.created_at.strftime(time_format))
        self.assertEqual(new_d["updated_at"],
                         b.updated_at.strftime(time_format))


if __name__ == "__main__":
    unittest.main()
