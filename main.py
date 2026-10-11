from shapes.circle import Circle
from shapes.rectangle import Rectangle
from shapes.triangle import Triangle



def main():
    shapes = [Circle(2), Rectangle(3, 4), Triangle(3, 4, 5)]
    for s in shapes:
        print(s.describe())


if __name__ == "__main__":
    main()