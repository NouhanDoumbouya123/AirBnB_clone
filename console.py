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
import json
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
        """Override the emptyline method"""
        pass

    def do_create(self, arg):
        """To create class"""
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
        print("create: Creates a new instance of BaseModel, \
              saves it (to the JSON file) and prints the id")

    def do_show(self, arg):
        """To show the class"""
        args = shlex.split(arg)
        if len(args) < 1:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
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
            print("** no instance found **")

    def do_destroy(self, arg):
        """To destroy an instance"""
        args = shlex.split(arg)
        if len(args) < 1:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
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
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Printing all instances of a class"""

        storage.reload()
        objects = storage.all()
        data = shlex.split(arg)
        my_json = []
        if not arg:
            for key in objects:
                my_json.append(str(objects[key]))
            print(json.dumps(my_json))
            return
        if data[0] in HBNBCommand.my_dict.keys():
            for key in objects:
                if data[0] in key:
                    my_json.append(str(objects[key]))
            print(json.dumps(my_json))
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute
        (save the change into the JSON file).
        Structure: update [class name] [id] [arg_name] [arg_value]
        """
        if not arg:
            print("** class name missing **")
            return
        my_data = shlex.split(arg)
        storage.reload()
        objs_dict = storage.all()
        if my_data[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        if len(my_data) == 1:
            print("** instance id missing **")
            return
        try:
            key = my_data[0] + "." + my_data[1]
            objs_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        if len(my_data) == 2:
            print("** attribute name missing **")
            return
        if len(my_data) == 3:
            print("** value missing **")
            return
        my_instance = objs_dict[key]
        if hasattr(my_instance, my_data[2]):
            data_type = type(getattr(my_instance, my_data[2]))
            setattr(my_instance, my_data[2], data_type(my_data[3]))
        else:
            setattr(my_instance, my_data[2], my_data[3])
        storage.save()

    def do_update_dict(self, arg):
        """update using a dictionary"""
        if not arg:
            print("** class name missing **")
            return
        my_dictionary = "{" + arg.split("{")[1]
        my_data = shlex.split(arg)
        storage.reload()
        objs_dict = storage.all()
        if my_data[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        if (len(my_data) == 1):
            print("** instance id missing **")
            return
        try:
            key = my_data[0] + "." + my_data[1]
            objs_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        if (my_dictionary == "{"):
            print("** attribute name missing **")
            return

        my_dictionary = my_dictionary.replace("\'", "\"")
        my_dictionary = json.loads(my_dictionary)
        my_instance = objs_dict[key]
        for my_key in my_dictionary:
            if hasattr(my_instance, my_key):
                data_type = type(getattr(my_instance, my_key))
                setattr(my_instance, my_key, my_dictionary[my_key])
            else:
                setattr(my_instance, my_key, my_dictionary[my_key])
        storage.save()

    def do_count(self, arg):
        """Count the objects"""
        count = 0
        storage.reload()
        objects = storage.all()
        args = shlex.split(arg)
        class_name = args[0]
        if class_name in HBNBCommand.my_dict.keys():
            for key in objects:
                if args[0] in key:
                    count += 1
        print(count)

    def default(self, arg):
        """When no command matched it"""
        val = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "update2": self.do_update_dict
        }
        arg = arg.strip()
        values = arg.split(".")
        if len(values) != 2:
            super().default(arg)
            return
        class_name = values[0]
        command = values[1].split("(")[0]
        if command == "update":
            if "{" in values[1]:
                command = "update_dict"
                args = values[1].split("(")[1].split(")")[0].split(", ", 1)
                if len(args) == 2:
                    command_line = f"{class_name} {args[0]} {args[1]}"
                    self.do_update_dict(command_line)
            args = values[1].split("(")[1].split(")")[0].split(", ")
            if len(args) == 3:
                command_line = f"{class_name} {args[0]} {args[1]} {args[2]}"
                self.do_update(command_line)
                return
        else:
            command_line = class_name
            if command in val.keys():
                args = values[1].split("(")[1].split(")")[0]
                command_line += " " + args
                val[command](command_line)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
