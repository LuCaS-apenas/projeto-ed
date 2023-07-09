import datetime
from directory import *

class File:

    def __init__(self, name: str, type: str, description: str,
                 content: str, size: str, directory: Directory):
        self.name = name
        self.type = type
        self.description = description
        self.size = size
        self.content = content
        self.creation = datetime.datetime.now ()
        self.directory = directory

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):
        self.__content = content

    @property
    def creation(self):
        return self.__creation

    @creation.setter
    def creation(self, creation):
        self.__creation = creation

    @property
    def directory(self):
        return self.__directory

    @directory.setter
    def directory(self, directory):
        self.__directory = directory

    def __str__(self):
        return f'''{self.name}.{self.type}'''
