import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit_present(self, mock_stdout):
        with patch('builtins.input', side_effect=['quit']):
            HBNBCommand().cmdloop()
            self.assertEqual(mock_stdout.getvalue(), "(hbnb) ")

    @patch('sys.stdout', new_callable=StringIO)
    def test_EOF_present(self, mock_stdout):
        with patch('builtins.input', side_effect=['EOF']):
            HBNBCommand().cmdloop()
            self.assertEqual(mock_stdout.getvalue(), "\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_present(self, mock_stdout):
        with patch('builtins.input', side_effect=['help']):
            HBNBCommand().cmdloop()
            self.assertTrue("documenting the commands" in mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_empty_line_present(self, mock_stdout):
        with patch('builtins.input', side_effect=['']):
            HBNBCommand().cmdloop()
            self.assertEqual(mock_stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_BaseModel_present(self, mock_stdout):
        with patch('builtins.input', side_effect=['create BaseModel']):
            HBNBCommand().cmdloop()
            self.assertTrue("missing" in mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_BaseModel_present(self, mock_stdout):
        with patch('builtins.input', side_effect=['show BaseModel 1234']):
            HBNBCommand().cmdloop()
            self.assertTrue("no instance found" in mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_BaseModel_present(self, mock_stdout):
        with patch('builtins.input', side_effect=['destroy BaseModel 1234']):
            HBNBCommand().cmdloop()
            self.assertTrue("no instance found" in mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_BaseModel_present(self, mock_stdout):
        with patch('builtins.input', side_effect=['all BaseModel']):
            HBNBCommand().cmdloop()
            self.assertEqual(mock_stdout.getvalue(), "[]\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_count_BaseModel_present(self, mock_stdout):
        with patch('builtins.input', side_effect=['count BaseModel']):
            HBNBCommand().cmdloop()
            self.assertEqual(mock_stdout.getvalue(), "0\n")

    # Similar test cases for User, State, City, Amenity, Place, Review

    # Test cases for show command for User, State, City, Amenity, Place, Review
    @patch('sys.stdout', new_callable=StringIO)
    def test_show_User_present(self, mock_stdout):
        with patch('builtins.input', side_effect=['show User 1234']):
            HBNBCommand().cmdloop()
            self.assertTrue("no instance found" in mock_stdout.getvalue())

    # Additional test cases for other commands...

if __name__ == '__main__':
    unittest.main()

