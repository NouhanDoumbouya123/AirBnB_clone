#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
from models import storage
from models.base_model import BaseModel
import cmd
import sys


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
        print("syntax: quit\
               -- terminates the application")

    def do_EOF(self, arg):
        """Translating the EOF"""
        print()
        sys.exit(127)

    def help_EOF(self):
        """documenting the commands"""
        print("syntax: ctrl + D\
              --terminates the application")

    def emptyline(self):
        """Overide the emptyline method"""
        return

    def do_create(self, name):
        if name == "" or name == None:
            print("** class name missing **")
        else:
            cls = globals().get(name)
            if cls:
                my_model = cls()
                my_model.save()
                print(my_model)
            else:
                print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
