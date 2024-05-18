#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
import sys
from models.base_model import BaseModel
from models.base_model import storage


class HBNBCommand(cmd.Cmd):
    """A command line simulation"""
    def __init__(self):
        """initiate the object"""
        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb) "

    def do_quit(self, arg):
        """The quit command"""
        sys.exit()

    def help_quit(self):
        """documenting the commands"""
        print("syntax: Quit command to exit the program")

    def do_EOF(self, arg):
        """Translating the EOF"""
        sys.exit(127)

    def help_EOF(self):
        """documenting the commands"""
        print("syntax: ctrl + D\
              --terminates the application")

    def emptyline(self):
        """Overide the emptyline method"""
        return

    def do_all(self, arg):
        """Printing all instances of base"""
        classes = {
                'BaseModel': BaseModel,
                }
        objects = storage.all()
        if arg:
            class_name = arg.strip()
            if class_name not in classes:
                print("** class doesn't exist **")
                return
            results = [str(obj) for obj in objects.values() if obj.__class__.__name__ == class_name]
        else:
            result = [str(obj) for obj in objects.values()]
        print(result)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
