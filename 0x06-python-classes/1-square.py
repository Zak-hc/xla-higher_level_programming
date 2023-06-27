#!/usr/bin/python3
class Square:
    """
    Represents a square.

    The Square class defines a square object with a single attribute, size.
    It provides a way to create square instances with a specified size.

    Args:
        size (int): The size of the square.

    Attributes:
        __size (int): The size of the square (private).

    """
    def __init__(self, size):
        self.__size = size
