# Rectangle.py
import  math
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def diagonaal(self):
        return math.sqrt(math.pow(self.width, 2) + math.pow(self.height, 2))