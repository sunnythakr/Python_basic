#  "Shape" superclass and its subclasses, like "Circle" and "Rectangle". 
# Each subclass has its own implementation of methods like area() 
# and perimeter()
class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

def print_shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

# Create instances of different shapes
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Using polymorphism to treat different shapes uniformly
print("Circle:")
print_shape_info(circle)

print("\nRectangle:")
print_shape_info(rectangle)
