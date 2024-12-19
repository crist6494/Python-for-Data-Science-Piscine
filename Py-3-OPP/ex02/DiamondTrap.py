from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representation of King family"""

    def __init__(self, first_name: str):
        """Constructor for King family
            Inherit the attributes of Baratheon and Lannister
        """
        super().__init__(first_name)

    def set_eyes(self, eyes):
        """Method to set the eyes attribute"""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """Method to set the hairs attribute"""
        self.hairs = hairs

    def get_eyes(self):
        """Method to get the eyes attribute"""
        return self.eyes

    def get_hairs(self):
        """Method to get the hairs attribute"""
        return self.hairs
