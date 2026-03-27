class Vehicle:
    """
    Базовый класс транспортного средства.

    Атрибуты:
        _brand (str): Марка транспортного средства
        _model (str): Модель транспортного средства
        _year (int): Год выпуска
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Инициализация транспортного средства.

        Args:
            brand: Марка транспортного средства
            model: Модель транспортного средства
            year: Год выпуска
        """
        self._brand = brand
        self._model = model
        self._year = self._validate_year(year)

    def _validate_year(self, year: int) -> int:
        """
        Защищенный метод для валидации года выпуска.

        Args:
            year: Год для проверки

        Raises:
            ValueError: Если год некорректный
        """
        import datetime
        current_year = datetime.datetime.now().year
        if year < 1900 or year > current_year + 1:
            raise ValueError(f"Год должен быть от 1900 до {current_year + 1}")
        return year

    def get_info(self) -> str:
        """
        Получение базовой информации.

        Returns:
            str: Информация о транспортном средстве
        """
        return f"{self._brand} {self._model} ({self._year})"

    def calculate_max_speed(self) -> float:
        """
        Расчет максимальной скорости.

        Returns:
            float: Максимальная скорость
        """
        return 0.0

    def __str__(self) -> str:
        return f"Транспортное средство: {self.get_info()}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self._brand!r}, model={self._model!r}, year={self._year!r})"


class Car(Vehicle):
    """
    Класс легкового автомобиля.

    Атрибуты:
        _horsepower (int): Мощность двигателя
        _fuel_type (str): Тип топлива
    """

    def __init__(self, brand: str, model: str, year: int, horsepower: int, fuel_type: str) -> None:
        """
        Инициализация легкового автомобиля.

        Args:
            brand: Марка
            model: Модель
            year: Год выпуска
            horsepower: Мощность в л.с.
            fuel_type: Тип топлива
        """
        super().__init__(brand, model, year)
        self._horsepower = self._validate_horsepower(horsepower)
        self._fuel_type = self._validate_fuel_type(fuel_type)

    def _validate_horsepower(self, horsepower: int) -> int:
        if not isinstance(horsepower, int) or horsepower < 1 or horsepower > 2000:
            raise ValueError("Мощность должна быть от 1 до 2000 л.с.")
        return horsepower

    def _validate_fuel_type(self, fuel_type: str) -> str:
        valid_types = ["бензин", "дизель", "электро", "гибрид"]
        if fuel_type.lower() not in valid_types:
            raise ValueError(f"Тип топлива должен быть: {valid_types}")
        return fuel_type.lower()

    def calculate_max_speed(self) -> float:
        """
        Перегрузка метода расчета скорости для легкового автомобиля.

        Returns:
            float: Максимальная скорость
        """
        return self._horsepower * 0.5 + 150

    def calculate_fuel_consumption(self, distance: float) -> float:
        """
        Расчет расхода топлива.

        Args:
            distance: Расстояние в км

        Returns:
            float: Расход топлива в литрах
        """
        return (distance / 100) * 8.0

    def __str__(self) -> str:
        return f"Легковой автомобиль: {self.get_info()}, {self._horsepower} л.с., {self._fuel_type}"

    def __repr__(self) -> str:
        return (f"Car(brand={self._brand!r}, model={self._model!r}, year={self._year!r}, "
                f"horsepower={self._horsepower!r}, fuel_type={self._fuel_type!r})")


class Truck(Vehicle):
    """
    Класс грузового автомобиля.

    Атрибуты:
        _load_capacity (float): Грузоподъемность в тоннах
        _axles (int): Количество осей
    """

    def __init__(self, brand: str, model: str, year: int, load_capacity: float, axles: int) -> None:
        """
        Инициализация грузового автомобиля.

        Args:
            brand: Марка
            model: Модель
            year: Год выпуска
            load_capacity: Грузоподъемность в тоннах
            axles: Количество осей
        """
        super().__init__(brand, model, year)
        self._load_capacity = self._validate_load_capacity(load_capacity)
        self._axles = self._validate_axles(axles)

    def _validate_load_capacity(self, load_capacity: float) -> float:
        if not isinstance(load_capacity, (int, float)) or load_capacity < 0.1 or load_capacity > 100:
            raise ValueError("Грузоподъемность должна быть от 0.1 до 100 тонн")
        return float(load_capacity)

    def _validate_axles(self, axles: int) -> int:
        if not isinstance(axles, int) or axles < 2 or axles > 5:
            raise ValueError("Количество осей должно быть от 2 до 5")
        return axles

    def calculate_max_speed(self) -> float:
        """
        Перегрузка метода расчета скорости для грузового автомобиля.

        Returns:
            float: Максимальная скорость
        """
        return max(70.0, 120.0 - self._load_capacity * 0.7)

    def calculate_max_payload(self) -> float:
        """
        Расчет полезной нагрузки.

        Returns:
            float: Полезная нагрузка в тоннах
        """
        return self._load_capacity * (1 + 0.1 * self._axles)

    def __str__(self) -> str:
        return (f"Грузовой автомобиль: {self.get_info()}, "
                f"грузоподъемность {self._load_capacity} т, {self._axles} оси")

    def __repr__(self) -> str:
        return (f"Truck(brand={self._brand!r}, model={self._model!r}, year={self._year!r}, "
                f"load_capacity={self._load_capacity!r}, axles={self._axles!r})")


if __name__ == "__main__":
    # Создание объектов
    car = Car("Toyota", "Camry", 2020, 249, "бензин")
    truck = Truck("Volvo", "FH16", 2019, 25.5, 3)

    # Демонстрация работы
    print(car)
    print(truck)
    print()

    print(f"Макс. скорость легкового: {car.calculate_max_speed():.1f} км/ч")
    print(f"Макс. скорость грузового: {truck.calculate_max_speed():.1f} км/ч")
    print()

    print(f"Расход топлива (100 км): {car.calculate_fuel_consumption(100):.1f} л")
    print(f"Полезная нагрузка: {truck.calculate_max_payload():.1f} т")
    print()

    print(repr(car))
    print(repr(truck))
