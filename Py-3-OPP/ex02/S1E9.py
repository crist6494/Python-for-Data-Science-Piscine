from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Abstract Class"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Your docstring for Constructor"""

        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Abstract method to be implemented by subclasses
        """
        pass


class Stark(Character):
    """Your docstring for Class"""

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False
