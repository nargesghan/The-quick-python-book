'''Modify the Rectangle class’s code to make the dimension variables private. What
restriction will this modification impose on using the class?
'''

#The dimension variables will no longer be accessible outside the class via .width , .height

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, delta_x, delta_y):
        self.x = self.x + delta_x
        self.y = self.y + delta_y

class Rectangle(Shape):
    def __init__(self,x=0,y=0,width=1,height=1):
        super().__init__(x,y)
        self.__width=width
        self.__height=height
    
    def area(self):
        return self.__width * self.__height