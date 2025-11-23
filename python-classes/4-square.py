#!/usr/bin/python3
"""This is documentation of the class."""


class Square:
    """This is a Square class."""

    def __init__(self, size=0):
        """Initialize the square with optional size."""
        self.size = size

    @property
    def size(self):
        """Retrieve size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using # characters."""
        if self.size == 0:
            print()
            return
        for _ in range(self.size):
            print("#" * self.size)
