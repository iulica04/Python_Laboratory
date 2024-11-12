# Create a class hierarchy for shapes, starting with a base class Shape.
# Then, create subclasses like Circle, Rectangle, and Triangle. Implement methods to calculate area and perimeter for each shape.

import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


if __name__ == '__main__':
    circle = Circle(10)
    print("Circle:")
    print("Area:", circle.area())
    print("Perimeter:", circle.perimeter())
    print()

    rectangle = Rectangle(10, 20)
    print("Rectangle:")
    print("Area:", rectangle.area())
    print("Perimeter:", rectangle.perimeter())
    print()

    triangle = Triangle(10, 20, 15)
    print("Triangle:")
    print("Area:", triangle.area())
    print("Perimeter:", triangle.perimeter())
    print()
