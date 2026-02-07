# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from abc import ABC, abstractmethod
from typing import Optional


class Vehicle(ABC):
    def __init__(self, max_speed: float, capacity: int, fuel_type: str) -> None:
        self.max_speed = max_speed
        self.capacity = capacity
        self.fuel_type = fuel_type

    @abstractmethod
    def move(self, distance: float) -> float:
        ...

    @abstractmethod
    def refuel(self, amount: float) -> float:
        ...

    @abstractmethod
    def get_info(self) -> dict:
        ...


class SocialNetwork(ABC):
    def __init__(self, name: str, active_users: int, foundation_year: int) -> None:
        self.name = name
        self.active_users = active_users
        self.foundation_year = foundation_year

    @abstractmethod
    def create_post(self, user_id: str, content: str, post_type: str = "text") -> str:
        ...

    @abstractmethod
    def add_friend(self, user_id: str, friend_id: str) -> bool:
        ...

    @abstractmethod
    def get_statistics(self, period_days: int = 30) -> dict:
        ...


class Furniture(ABC):
    def __init__(self, material: str, dimensions: tuple[float, float, float], weight: float) -> None:
        self.material = material
        self.dimensions = dimensions
        self.weight = weight

    @abstractmethod
    def assemble(self, tools: list[str]) -> bool:
        ...

    @abstractmethod
    def calculate_load_capacity(self, surface_type: str) -> Optional[float]:
        ...

    @abstractmethod
    def get_volume(self) -> float:
        ...


if __name__ == "__main__":
    doctest.testmod()



    