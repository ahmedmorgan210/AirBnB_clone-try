#!/usr/bin/python3
"""lets play with stor"""
import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "City": City,
    "Place": Place,
    "Amenity": Amenity,
    "Review": Review,
    "State": State
    }

class FileStorage:
    """the store to by"""
    def __init__(self) -> None:
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """thats all"""
        return self.__objects

    def new(self, obj):
        """omg its new"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """keep at order"""
        data_dict = {}
        data_str = ""

        for key, value in self.__objects.items():
            data_dict[key] = value.to_dict()

        data_str = json.dumps(data_dict)

        with open(self.__file_path, 'w') as file:
            file.write(data_str)
        # with open(self.__objects, mode='w', encoding='UTF-8') as file:
        #     self.__file_path = json.dump(data, file)


        # with open("file.json", mode="w") as file:
        #     data = {}
        #     for key, value in self.__objects:
        #         data[key] = value.to_


        # with open("file.json", mode="w") as file:
        #     json.dump(self.__objects, file)
        # self.__file_path = "../../{file}"
    
    def reload(self):
        """try to be again"""
        try:
            with open(FileStorage.__file_path, 'r') as data_json:
                FileStorage.__objects = json.load(data_json)
                for k, v in FileStorage.__objects.items():
                    FileStorage.__objects[k] = classes[v['__class__']](**v)
        # try:
        #     with open(self.__file_path, 'r') as f:
        #         if os.path.isfile(f):
        #             self.__objects = json.loads(f)
        except Exception:
            pass
