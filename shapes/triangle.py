import math

from shapes.shape import Shape


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        super().__init__("Triangle")
        self.a, self.b, self.c = a, b, c

    def perimeter(self) -> float:
        return self.a + self.b + self.c

    def area(self) -> float:
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
