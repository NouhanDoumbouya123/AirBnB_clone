#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

    def test_do_nothing(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("nothing")
            self.assertEqual(f.getvalue(), "")

    def test_do_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            result = HBNBCommand().onecmd("quit")
            self.assertTrue(result)
    
    def test_help_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertIn("Quit command to exit the program", f.getvalue())

    def test_do_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            result = HBNBCommand().onecmd("EOF")
            self.assertTrue(result)
            self.assertIn("\n", f.getvalue())

    def test_help_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertIn("terminates the application", f.getvalue())

    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual(f.getvalue(), "")

    def test_do_create_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertIn("** class name missing **", f.getvalue())

    def test_do_create_nonexistent_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create NonExistentClass")
            self.assertIn("** class doesn't exist **", f.getvalue())

    def test_do_show_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertIn("** class name missing **", f.getvalue())

    def test_do_show_missing_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertIn("** instance id missing **", f.getvalue())

    def test_do_show_nonexistent_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show NonExistentClass 1234")
            self.assertIn("** class doesn't exist **", f.getvalue())

    def test_do_show_no_instance_found(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 1234")
            self.assertIn("** no instance found **", f.getvalue())

    # Add more tests for other methods like do_destroy, do_all, do_update, etc.

if __name__ == '__main__':
    unittest.main()
