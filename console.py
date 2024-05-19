#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
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
        print("Quit command to exit the program")

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

    def do_create(self, arg):
        """To create instances"""
        if not arg:
            print("** class name missing **")
        else:
            cls = globals().get(arg)
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
        """To show the instances"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            name, id = args
        cls = globals().get(name)
        if cls is None:
            print("** class doesn't exist **")
            return
        count = 0
        storage.reload()
        objects = storage.all()
        key = f"{name}.{id}"
        if key in objects:
            print(str(objects[key]))
            count += 1
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """To destroy an instance"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        else:
            name, id = args
        cls = globals().get(name)
        if cls is None:
            print("** class doesn't exist **")
        storage.reload()
        objects = storage.all()
        key = f"{name}.{id}"
        if key in objects:
            del(objects[key])
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Printing all instances of base"""
        classes = {
                'BaseModel': BaseModel,
                'User': User,
                }
        storage.reload()
        objects = storage.all()
        if arg:
            class_name = arg.strip()
            if class_name not in classes:
                print("** class doesn't exist **")
                return
            results = [str(obj) for obj in objects.values()
                       if obj.__class__.__name__ == class_name]
        else:
            results = [str(obj) for obj in objects.values()]
        print(results)

    def do_update(self, arg):
        """Update an instance based on class name and id"""
        args = arg.split()[:4]

        if len(args) < 1:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        else:
            class_name, obj_id, attr_name, attr_value = args

        # Remove double quotes from attribute value if present
        if attr_value.startswith('"') and attr_value.endswith('"'):
            attr_value = attr_value[1:-1]

            # Check if class exists
            cls = globals().get(class_name)
            if not cls:
                print("** Class doesn't exist **")
                return

            # Check if instance exists
            key = f"{class_name}.{obj_id}"
            if key not in storage.all():
                print("** Instance not found **")
                return

            # Check if attribute exists in the class
            if class_name != "BaseModel":
                if not hasattr(cls, attr_name):
                    print(f"** Attribute '{attr_name}' doesn't exist"
                          f" for class '{class_name}' **")
                    return

            # Get the instance
            storage.reload()
            instance = storage.all()[key]

            # Check if the attribute is id, created_at
            # or updated_at (which cannot be updated)
            if attr_name in ["id", "created_at", "updated_at"]:
                print("** Cannot update 'id', "
                      "'created_at', or 'updated_at' **")
                return

            # Cast attribute value to the attribute type
            try:
                attr_type = type(getattr(cls, attr_name))
                attr_value = attr_type(attr_value)
            except ValueError:
                print("** Invalid value type for the attribute **")
                return
            except AttributeError:
                pass

            # Update the attribute value and save the changes
            setattr(instance, attr_name, attr_value)
            instance.save()

    def default(self, line):
        """Handle the default unrecognized command"""
        parts = line.split(".")
        if len(parts) == 2:
            class_name, command = parts
            if command == "all()":
                self.do_all(class_name)
            else:
                print("Unknown syntax")
        else:
            print("Enter the correct number of command")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
