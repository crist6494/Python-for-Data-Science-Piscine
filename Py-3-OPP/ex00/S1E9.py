from abc import ABC, abstractmethod


class Character(ABC):
    "Your docstring for Abstract Class"

    def __init__(self, name: str, is_alive: bool=True):
        self.name = name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        pass


class Stark(Character):
    "Your docstring for Class"

    def __init__(self, name: str, is_alive: bool=True):
        "Your docstring for Constructor"
        super().__init__(name, is_alive)

    def die(self):
        "Your docstring for Method"
        self.is_alive = False
