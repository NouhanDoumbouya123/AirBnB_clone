#!/usr/bin/python3
"""Test BaseModel for expected behavior and documentation"""
import unittest
from unittest.mock import patch
from datetime import datetime
import uuid
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../..')))
BaseModel = __import__('models').base_model.BaseModel


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""
    def setUp(self):
        """Set up for the tests"""
        self.base_model = BaseModel()

    def test_init(self):
        """testing the initiation of the object"""
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)
        self.assertEqual(self.base_model.created_at,
                         self.base_model.updated_at)

    def test_init_with_kwargs(self):
        """Test initialization with kwargs"""
        id = str(uuid.uuid4())
        now = datetime.now().isoformat()
        kwargs = {
            "id": id,
            "created_at": now,
            "updated_at": now,
        }
        model = BaseModel(**kwargs)
        self.assertEqual(model.id, id)
        self.assertEqual(model.created_at, datetime.fromisoformat(now))
        self.assertEqual(model.updated_at, datetime.fromisoformat(now))

    def test_str(self):
        """Test the __str__ method"""
        expected_str = (
            f"[BaseModel] ({self.base_model.id}) "
            f"{self.base_model.__dict__}"
        )
        self.assertEqual(str(self.base_model), expected_str)

    def test_save(self):
        """Test the save method"""
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str(self):
        """Tests the __str__ method"""
        expected_str = f"[BaseModel]\
 ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_str)

    def test_to_dict(self):
        """Test the to_dict method"""
        model_dict = self.base_model.to_dict()
        self.assertEqual(model_dict["id"], self.base_model.id)
        self.assertEqual(
            model_dict["created_at"],
            self.base_model.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        )
        self.assertEqual(
            model_dict["updated_at"],
            self.base_model.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        )
        self.assertEqual(model_dict["__class__"], "BaseModel")

    @patch('models.storage.save')
    def test_storage_save_called(self, mock_save):
        """Test that storage.save is called during save"""
        self.base_model.save()
        mock_save.assert_called_once()

    @patch('models.storage.new')
    @patch('models.storage.save')
    def test_storage_new_called(self, mock_save, mock_new):
        """
        Test that storage.new is called during initialization without kwargs
        """
        model = BaseModel()
        mock_new.assert_called_once_with(model)
        mock_save.assert_called_once()


if __name__ == '__main__':
    unittest.main()
