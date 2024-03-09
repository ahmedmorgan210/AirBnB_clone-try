#!/usr/bin/python3
"""lets play with stor"""
import json
import os.path


class FileStorage:
    """the store to by"""
    def __init__(self) -> None:
        self.file_path = ""
        self.objects = {}

    @property
    def file_path(self):
        return self.__file_path

    @file_path.setter
    def file_path(self, value):
        self.__file_path = value

    @property
    def objects(self):
        return self.__objects

    @objects.setter
    def objects(self, value):
        self.__objects = value

    def all(self):
        """thats all"""
        return self.__objects

    def new(self, obj):
        """omg its new"""
        self.__objects.__dict__[__class__.__name__.id] = obj

    def save(self):
        """keep at order"""
        with open("file.json", mode="w") as file:
            json.dump(self.__objects, file)
        self.file_path = file
    
    def reload(self):
        """try to be again"""
        try:
            if os.path.isfile(self.file_path):
                self.__objects = json.loads("file.json")
        except Exception:
            pass
