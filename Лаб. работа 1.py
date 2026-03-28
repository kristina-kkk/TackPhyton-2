# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from abc import ABC, abstractmethod
from typing import Dict


class Vehicle(ABC):
    """
    Абстрактный базовый класс для транспортных средств.
    """

    def __init__(self, max_speed: float, capacity: int, fuel_type: str) -> None:
        self.max_speed = max_speed
        self.capacity = capacity
        self.fuel_type = fuel_type

    @abstractmethod
    def move(self, distance: float) -> float:
        """
        Двигаться на заданное расстояние.

        >>> vehicle = Car(180, 5, "бензин")
        >>> vehicle.move(100)
        100.0
        """
        pass

    @abstractmethod
    def refuel(self, amount: float) -> float:
        """
        Заправить транспорт.

        >>> vehicle = Car(180, 5, "бензин")
        >>> vehicle.refuel(40)
        40.0
        """
        pass

    @abstractmethod
    def get_info(self) -> Dict[str, object]:
        """
        Получить информацию о транспорте.

        >>> vehicle = Car(180, 5, "бензин")
        >>> 'max_speed' in vehicle.get_info()
        True
        """
        pass


class Car(Vehicle):
    """Класс автомобиля."""

    def __init__(self, max_speed: float, capacity: int, fuel_type: str) -> None:
        super().__init__(max_speed, capacity, fuel_type)

    def move(self, distance: float) -> float:
        return distance

    def refuel(self, amount: float) -> float:
        return amount

    def get_info(self) -> Dict[str, object]:
        return {
            "max_speed": self.max_speed,
            "capacity": self.capacity,
            "fuel_type": self.fuel_type
        }


class Bike(Vehicle):
    """Класс мотоцикла."""

    def __init__(self, max_speed: float, capacity: int, fuel_type: str) -> None:
        super().__init__(max_speed, capacity, fuel_type)

    def move(self, distance: float) -> float:
        return distance

    def refuel(self, amount: float) -> float:
        return amount

    def get_info(self) -> Dict[str, object]:
        return {
            "max_speed": self.max_speed,
            "capacity": self.capacity,
            "fuel_type": self.fuel_type
        }


class Truck(Vehicle):
    """Класс грузовика."""

    def __init__(self, max_speed: float, capacity: int, fuel_type: str) -> None:
        super().__init__(max_speed, capacity, fuel_type)

    def move(self, distance: float) -> float:
        return distance

    def refuel(self, amount: float) -> float:
        return amount

    def get_info(self) -> Dict[str, object]:
        return {
            "max_speed": self.max_speed,
            "capacity": self.capacity,
            "fuel_type": self.fuel_type
        }


if __name__ == "__main__":
    doctest.testmod(verbose=True)


