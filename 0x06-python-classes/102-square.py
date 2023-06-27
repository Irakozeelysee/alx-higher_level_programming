class Square:
    """
    This class represents a square.

    Attributes:
        __size (float or int): The size of the square.

    Methods:
        __init__(self, size=0):
            Initializes a new instance of the Square class with a given size.
        size(self):
            Getter method to retrieve the size of the square.
        size(self, value):
            Setter method to set the size of the square.
        area(self):
            Calculates and returns the current square area.
        __eq__(self, other):
            Determines if two squares are equal based on their areas.
        __ne__(self, other):
            Determines if two squares are not equal based on their areas.
        __lt__(self, other):
            Determines if the area of the current square
            is less than the area of another square.
        __le__(self, other):
            Determines if the area of the current square
            is less than or equal to the area of another square.
        __gt__(self, other):
            Determines if the area of the current square
            is greater than the area of another square.
        __ge__(self, other):
            Determines if the area of the current square
            is greater than or equal to the area of another square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class with a given size.

        Args:
            size (float or int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Args:
            value (float or int): The size value to set.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            float or int: The calculated area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Determines if two squares are equal based on their areas.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the squares are equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Determines if two squares are not equal based on their areas.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the squares are not equal, False otherwise.
        """
        return not self.__eq__(other)

    def __lt__(self, other):
        """
        Determines if the area of the current square
        is less than the area of another square.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the current square
            is less than the other square, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """
        Determines if the area of the current square
        is less than or equal to the area of another square.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the current square
            is less than or equal to the other square, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

    def __gt__(self, other):
        """
        Determines if the area of the current square
        is greater than the area of another square.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the current square
            is greater than the other square, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """
        Determines if the area of the current square
        is greater than or equal to the area of another square.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the current square
            is greater than or equal to the other square, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented
