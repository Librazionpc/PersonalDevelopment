#!/usr/bin/python3
# Scripts the uses cmd module to run my application :)

import cmd

from models import storage
from models import base_model, user, state, city, amenity, place, review
BaseModel = base_model.BaseModel
User = user.User
State = state.State
City = city.City
Amenity = amenity.Amenity
Place = place.Place
Review = review.Review


def classes(class_name):
    """Returns all classes instance that are available
    """
    
    all_classes = {
        "BaseModel": BaseModel(),
        "User": User(),
        "State": State(),
        "City": City(),
        "Amenity": Amenity(),
        "Place": Place(),
        "Review": Review()
            }
    
    if class_name in all_classes:
        return all_classes[class_name]
    else:
        return None
    
class HBNBCommand(cmd.Cmd):


    def __init__(self):
        super().__init__()
        self.prompt = "(hbnb) "
        self.new_instance = None        
            
    def do_create(self, line):
        """Create a BaseModel Instance

        Args:
            line (string): read from stdin
        """
        args = line.split()
        
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        
        new_instance = classes(class_name)
        if new_instance is None:
            print("** class doesn't exist **")
            return
        print(new_instance.id)
        new_instance.save()
    
    def do_show(self, line):
        """Print the object of a particalar BaseModel ID

        Args:
            line (string): reads from stdin
        """
        
        if line is None:
            print("** class name missing **")
            return
        else:
            args = line.split()
            if len(args) == 0:
                print("** class name missing **")
                return
            elif classes(args[0]) is None:
                print("** class doesn't exist **")
                return
            elif args == 1:
                print("** instance id missing **")
                return
            else:
                storage.reload()
                key = "{}.{}".format(args[0], args[1])
                all_object = storage.all()
                
                if key in all_object:
                    if len (args) < 2:
                        print(all_object[key])
                    self.info = all_object[key]
                else:
                    print("** no instance found **")
                    return
   
    def do_all(self, line):
        if classes(line) == None and line is None:
            print("** class doesn't exist **")
            return
        else:
            print(storage.all())
    
    def do_update(self, line):
        args = line.split()
        self.do_show(line)
        if len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        else:
            attr_name = args[2]
            attr_value = " ".join(args[3:])
            self.info[attr_name] = attr_value
       
    
    def do_destroy(self, line):
        """Deletes a particalar BaseModel ID

        Args:
            line (string): reads from stdin
        """
        if line is None:
            print("** class name missing **")
            return
        else:
            args = line.split()
            if len(args) == 0:
                print("** class name missing **")
                return
            elif classes(args[0]) is None:
                print("** class doesn't exist **")
                return
            elif args == 1:
                print("** instance id missing **")
                return
            else:
                key = "{}.{}".format(args[0], args[1])
                result = storage.destroy(key)
                if result is None:
                    print("** no instance found **")
                    return
                                    
    def do_quit(self, line):
        print("Exitong program")
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
