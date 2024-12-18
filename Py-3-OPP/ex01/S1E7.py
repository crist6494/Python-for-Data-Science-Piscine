from S1E9 import Character


class Baratheon(Character):
    "Representation of Baratheon family"
    def __init__(self, first_name):
        super().__init__(first_name)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        self.is_alive = False

    def __repr__(self):
        return f"Vector: ('{self.__class__.__name__}', '{self.eyes}', '{self.hairs}')"
    
    def __str__(self):
        return f"${self.__repr__}"
    

class Lannister(Character):
    def __init__(self, first_name, is_alived=True):
        super().__init__(first_name, is_alived)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"
    
    def die(self):
        self.is_alive = False

    def __repr__(self):
        return f"Vector: ('{self.__class__.__name__}', '{self.eyes}', '{self.hairs}')"
    
    def __str__(self):
        return f"${self.__repr__}"

    @classmethod
    def create_lannister(cls, first_name: str, is_alived: bool):
        return cls(first_name, is_alived)