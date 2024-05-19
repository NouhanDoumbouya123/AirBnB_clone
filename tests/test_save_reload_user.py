#!/usr/bin/python3
import unittest
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_init(self):
        self.assertIsInstance(self.user, User)
        # Add more assertions to test the initialization of User attributes

    def test_str(self):
        expected_str = f"[User] ({self.user.id}) {self.user.__dict__}"
        self.assertEqual(str(self.user), expected_str)
        # Add more assertions if necessary

    def test_to_dict(self):
        expected_dict = {
            'id': self.user.id,
            'created_at': self.user.created_at.isoformat(),
            'updated_at': self.user.updated_at.isoformat(),
            '__class__': 'User',
            'email': '',
            'password': '',
            'first_name': '',
            'last_name': ''
        }
        self.assertEqual(self.user.to_dict(), expected_dict)
        # Add more assertions if necessary

    # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()
