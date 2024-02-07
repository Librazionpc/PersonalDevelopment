#!/usr/bin/python3
# Scripts that serializes and deserializes instances to JSON and deserializes JSON to instances
from os.path import isfile
import json

class FileStorage:
    """ Class that create new, saves to JSON {file.json} in __dict__ format, reload from {file.json}
        and delete objects
    """
    def __init__(self):
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        """Returns all object available"""
        return (self.__objects)

    def new(self, obj):
        """Create new object in dictionary format for JSON
        """
        self.cls_name = obj.__class__.__name__
        key = "{}.{}".format(self.cls_name, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """Write the all the created object to a file.json
        """
        serialized_obj = {}
        for keys, obj in self.__objects.items():
            serialized_obj[keys] = obj
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_obj, file)

    def reload(self):
        """Read for the file.json and convert bask to python format
        """
        if isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                data = json.loads(content)
                for key, value in data.items():
                    self.__objects[key] = value

    def destroy(self, key):
        """ Deletes object using it key and automatically saves it
        
        Returns:
            None if the key is not found
        """
        results = self.__objects.pop(key, None)
        self.save()
        
        return (results)
