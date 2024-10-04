from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        self.area = 0
        self.volume = 0

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_volume(self):
        pass

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
        self.calculate_area()
        self.calculate_volume()

    def calculate_area(self):
        self.area = self.length ** 2

    def calculate_volume(self):
        self.volume = 0  

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
        self.calculate_area()
        self.calculate_volume()

    def calculate_area(self):
        self.area = 3.14 * self.radius * self.radius

    def calculate_volume(self):
        self.volume = 0  

square = Square(5)
circle = Circle(5)

print(f"Square area: {square.area}")
print(f"Square volume: {square.volume}")
print(f"Circle area: {circle.area}")    
print(f"Circle volume: {circle.volume}")