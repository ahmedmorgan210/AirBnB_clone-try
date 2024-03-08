#!/usr/bin/python3
# Base cls
import uuid
import datetime


class BaseModel:
    """base is important"""
    def __init__(self):
        """hey it is ini"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self) -> str:
        """come to pri"""
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """rmmber me"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """open the book"""
        self.created_at = str(datetime.datetime.isoformat(self.created_at))
        self.updated_at = str(datetime.datetime.isoformat(self.updated_at))
        self.__dict__['__class__'] = __class__.__name__
        return self.__dict__
