#!/usr/bin/python3


"""nice people making nice questions nice I AM RAGE
BAITED"""


class Square:

    "people boss"

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        return self.__size ** 2

    def get_size(self):
        return self.__size
    
    def set_size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
    
    size = property(get_size, set_size)
