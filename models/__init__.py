#!/usr/bin/python3
"""the start poi"""
import imp


from models.engine import file_storage
storage = file_storage.FileStorage()
file_storage.FileStorage.reload(storage)


# from engine.file_storage import FileStorage
# #storage = file_storage.FileStorage()
# storage = FileStorage()