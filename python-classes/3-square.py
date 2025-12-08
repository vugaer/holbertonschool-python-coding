#!/usr/bin/python3

"""nice people making nice questions nice I AM RAGE
BAITED"""


class Square:

    "people boss"

    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        return self.__size ** 2

    def size(self, value=None):
        if value == None:
            return self.__size
        else:
            self.__size = value
