from shapes.circle import Circle


def main():
    shapes = [Circle(2)]
    for s in shapes:
        print(s.describe())


if __name__ == "__main__":
    main()
