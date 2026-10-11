from shapes.rectangle import Rectangle


def main():
    shapes = [Rectangle(3, 4)]
    for s in shapes:
        print(s.describe())


if __name__ == "__main__":
    main()
