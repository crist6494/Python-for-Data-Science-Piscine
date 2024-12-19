class calculator:
    """A class to represent a calculator"""

    def __init__(self, object) -> None:
        """Constructor for calculator class
            initializes a list of values
        """
        self.values = object

    def __add__(self, object) -> None:
        """Method to add a value to the list"""
        self.values = list(map(lambda x: x + object, self.values))
        print(self.values)

    def __sub__(self, object) -> None:
        """Method to subtract a value from the list"""
        self.values = list(map(lambda x: x - object, self.values))
        print(self.values)

    def __mul__(self, object) -> None:
        """Method to multiply a value to the list"""
        self.values = list(map(lambda x: x * object, self.values))
        print(self.values)

    def __truediv__(self, object) -> None:
        """Method to divide a value from the list"""
        try:
            self.values = list(map(lambda x: x / object, self.values))
            print(self.values)
        except ZeroDivisionError as e:
            print(f"{type(e).__name__}: {e}")
