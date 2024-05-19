#!/usr/bin/python3
"""Test BaseModel for expected behavior and documentation"""
import unittest
from unittest.mock import patch
from datetime import datetime
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
BaseModel = __import__('models').base_model.BaseModel


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""
    def setUp(self):
        """create the BaseModel object"""
        self.base_model = BaseModel()

    def test_init(self):
        """testing the initiation of the object"""
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save(self):
        """test the save method save"""
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test_str(self):
        """Tests the __str__ method"""
        expected_str = f"[BaseModel]\
 ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_str)

    def test_to_dict(self):
        """Test case for to_dict"""
        expected_dict = {
            'id': self.base_model.id,
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertEqual(self.base_model.to_dict(), expected_dict)

    @patch('models.storage.save')
    def test_storage_save_called(self, mock_save):
        """tests the strorage.save() call"""
        self.base_model.save()
        mock_save.assert_called_once()


if __name__ == '__main__':
    unittest.main()
