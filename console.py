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
import shlex
import cmd


class HBNBCommand(cmd.Cmd):
    """A command line simulation"""
    prompt = "(hbnb) "
    my_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
            }

    def do_nothing(self, arg):
        """Does nothing"""
        pass

    def do_quit(self, arg):
        """The quit command"""
        return True

    def help_quit(self):
        """documenting the commands"""
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """Translating the EOF"""
        print("")
        return True

    def help_EOF(self):
        """documenting the commands"""
        print("syntax: ctrl + D\
              --terminates the application")

    def emptyline(self):
        """Overide the emptyline method"""
        pass

    def do_create(self, arg):
        """To create clss"""
        if not arg:
            print("** class name missing **")
            return
        my_data = shlex.split(arg)
        if my_data[0] in HBNBCommand.my_dict.keys():
            my_model = HBNBCommand.my_dict[my_data[0]]()
            print(my_model.id)
            my_model.save()
        else:
            print("** class doesn't exist **")

    def help_create(self):
        print("create: Creates a new cls of BaseModel, \
              saves it (to the JSON file) and prints the id")

    def do_show(self, arg):
        """To show the clss"""
        args = shlex.split(arg)
        if len(args) < 1:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("** cls id missing **")
            return
        else:
            name, id = args
        if name not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        storage.reload()
        objects = storage.all()
        key = f"{name}.{id}"
        if key in objects:
            print(str(objects[key]))
        else:
            print("** no cls found **")

    def do_destroy(self, arg):
        """To destroy an cls"""
        args = shlex.split(arg)
        if len(args) < 1:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** cls id missing **")
            return
        else:
            name, id = args
        if name not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
        storage.reload()
        objects = storage.all()
        key = f"{name}.{id}"
        if key in objects:
            del(objects[key])
            storage.save()
        else:
            print("** no cls found **")

    def do_all(self, arg):
        """Printing all clss of base"""
        classes = {
                'BaseModel': BaseModel,
                'User': User,
                'Amenity': Amenity,
                'City': City,
                'Review': Review,
                'Place': Place,
                'State': State
                }
        storage.reload()
        objects = storage.all()
        data = shlex.split(arg)
        if data[0]:
            class_name = data[0].strip("")
            if class_name not in classes:
                print("** class doesn't exist **")
                return
            results = [str(obj) for obj in objects.values()
                       if obj.__class__.__name__ == class_name]
        else:
            results = [str(obj) for obj in objects.values()]
        print(results)

    def do_update(self, arg):
        """Update an cls based on class name and id"""
        args = shlex.split()[:4]

        if len(args) < 1:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("** cls id missing **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        else:
            class_name, obj_id, attr_name, attr_value = args

        # Check if class exists
        if class_name not in HBNBCommand.my_dict.keys():
            print("** Class doesn't exist **")
            return

        # Check if cls exists
        key = f"{class_name}.{obj_id}"
        if key not in storage.all():
            print("** no cls found **")
            return

        storage.reload()
        cls = storage.all()[key]

        # Check if attribute exists in the class
        if class_name != "BaseModel":
            if not hasattr(cls, attr_name):
                print(f"** Attribute '{attr_name}' doesn't exist"
                        f" for class '{class_name}' **")
                return

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
        setattr(cls, attr_name, attr_value)
        cls.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
