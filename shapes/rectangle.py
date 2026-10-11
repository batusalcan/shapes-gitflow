from shapes.shape import Shape


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
