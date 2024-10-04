class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius

circle = Circle(5)
print(f"Area of circle: {circle.area()}")
print(f"Circumference of circle: {circle.circumference()}")