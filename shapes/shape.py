from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def area(self) -> float:
        ...

    @abstractmethod
    def perimeter(self) -> float:
        ...

    def describe(self) -> str:
        return f"{self.name}: area={self.area():.2f}, perimeter={self.perimeter():.2f}"
