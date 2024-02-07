#!/usr/bin/python3
"""Scripts that deals with the Class [BaseModel]
   That also create the dict for all object for
   serialization and deserialization 
"""

from models import storage
from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            kwargs['__class__'] = type(self).__name__
            kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f"
                    )
            kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f"
                    )

            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __setattr__(self, name, value):
        if name != "updated_at":
            self.updated_at = datetime.now()
        super().__setattr__(name, value)

    def __str__(self):
        other = self.__dict__
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        object_dict = self.__dict__.copy()
        object_dict["__class__"] = type(self).__name__
        object_dict["created_at"] = self.created_at.isoformat()
        object_dict["updated_at"] = self.updated_at.isoformat()
        return object_dict

