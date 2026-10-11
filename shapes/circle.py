import math

from shapes.shape import Shape


class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("radius must be positive")
        super().__init__("Circle")
        self.radius = radius


    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
