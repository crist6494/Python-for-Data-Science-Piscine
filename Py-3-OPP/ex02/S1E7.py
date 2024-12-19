from S1E9 import Character


class Baratheon(Character):
    """Representation of Baratheon family"""

    def __init__(self, first_name: str):
        """Constructor for Baratheon family
            initializes the atrributes of the class
        """
        super().__init__(first_name)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """
        Method to set the is_alive attribute to False
        """
        self.is_alive = False

    def __repr__(self):
        """Representation of the class"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __str__(self):
        """String representation of the class"""
        return f"${self.__repr__}"


class Lannister(Character):
    """Representation of Lannister family"""

    def __init__(self, first_name, is_alive=True):
        """Constructor for Baratheon family
            initializes the atrributes of the class
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """
        Method to set the is_alive attribute to False
        """
        self.is_alive = False

    def __repr__(self):
        """Representation of the class"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __str__(self):
        """String representation of the class"""
        return f"${self.__repr__}"

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool):
        """Class method to create Lannister family"""
        return cls(first_name, is_alive)
