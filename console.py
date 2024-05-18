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
                print(my_model.id)
            else:
                print("** class doesn't exist **")

    def help_create(self):
        print("create: Creates a new instance of BaseModel, \
              saves it (to the JSON file) and prints the id")

    def do_show(self, arg):
        name, id = arg.split()
        if not name:
            print("** instance id is missing **")
            return
        elif not id:
            print("** class name missing **")
            return
        cls = globals().get(name)
        if cls is None:
            print("** class doesn't exist **")
            return
        count = 0
        objects = storage.all()
        if f"{name}.{id}" in objects.keys():
            print(cls())
            count += 1
        if count == 0:
            print("** no instance found **")

    def do_destroy(self, arg):
        name, id = arg.split()
        if not name:
            print("** class name is missing **")
        if not id:
            print("** instance id missing **")
        cls = globals().get(name)
        if cls is None:
            print("** class doesn't exist **")

        objects = storage.all()
        key = f"{name}.{id}"
        if key in objects.keys():
            objects.pop(key)
            storage.save()
        else:
            print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
