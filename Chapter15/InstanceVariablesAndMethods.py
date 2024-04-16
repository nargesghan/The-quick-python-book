'''Update the code for a Rectangle class so that you can set the dimensions when an
instance is created, just as for the Circle class above. Also, add an area() method.'''

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

rectangle = Rectangle(12, 2)
print(rectangle.area())
