#!/usr/bin/python3
import os
import sys
sys.path.append('../../')
from models.base_model import BaseModel


my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89

print(my_model)

my_model.save()
print(my_model)

my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    key_type = type(my_model_json[key])
    print("\t{}: ({}) - {}".format(key, key_type, my_model_json[key]))
