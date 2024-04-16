'''Update the dimensions of the Rectangle class to be properties with getters and
setters that don’t allow negative sizes'''

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, delta_x, delta_y):
        self.x = self.x + delta_x
        self.y = self.y + delta_y

class Rectangle(Shape):
    def __init__(self,width,height,x=0,y=0):
        super().__init__(x,y)
        self.__width=width
        self.__height=height
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self,new_width):
        if new_width>=0:
            self.__width=new_width

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,new_height):
        if new_height>=0:
            self.__height=new_height

    
    def area(self):
        return self.__width * self.__height


rec=Rectangle(1,2)
print(rec.width)