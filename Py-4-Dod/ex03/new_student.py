import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate random string with 15 characters"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Student created with dataclass
    """
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(init=False, default=True)
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """Create login from name and surname"""
        self.login = self.name[0].upper() + self.surname.lower()
