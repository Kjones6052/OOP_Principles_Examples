
import math

class Shape:
    def calculate_area(self):
        raise NotImplementedError("Calculate area method not implemented.")
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius **2
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height
    
def get_area(shape):
    if isinstance(shape, Shape):
        return shape.calculate_area()
    else:
        raise TypeError("Invalid shape type.")
    
def main():
    circle = Circle(5)
    rectangle = Rectangle(10, 5)
    triangle = Triangle(10, 8)

    shapes = [circle, rectangle, triangle]
    for shape in shapes:
        try:
            area = get_area(shape)
            print(f"The area of {shape.__class__,__name__} is {area}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()