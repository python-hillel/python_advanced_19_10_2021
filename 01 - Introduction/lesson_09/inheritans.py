class Shape:
    VAR1 = 0
    h = 10

    def __init__(self, x, y):
        self.h = 6
        self.x = x
        self.y = y

    def draw(self):
        pass

    def rotate(self):
        pass

    def scaling(self):
        pass


class Circle(Shape):
    def __init__(self, XX, YY, radius):
        # Shape.__init__(self, XX, YY)
        # super().VAR1 = 9
        super().__init__(XX, YY)
        # self.x = x
        # self.y = y
        self.radius = radius


class Rectangle(Shape):
    # h = 0
    w = 0

    def __init__(self):
        super().__init__(3, 5)
        # self.h = 9
        self.w = 8


class Polygon(Shape):
    lst = []


c = Circle(4, 6, 7)
print(dir(c))

r = Rectangle()
print(r.h)
