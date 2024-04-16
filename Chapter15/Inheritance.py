'''Rewrite the code for a Rectangle class to inherit from Shape. Because squares and
rectangles are related, would it make sense to inherit one from the other? If so, which
would be the base class, and which would inherit?
'''
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
        self.width=width
        self.height=height
    
    def area(self):
        return self.width * self.height


req=Rectangle(2,3,12,10)
print(req.width)
print(req.x)


class Square(Rectangle):
    def __init__(self,side,x=0,y=0):
        super().__init__(x,y,side, side)


sq=Square(12)

print(sq.area())
print(sq.height)


'''How would you write the code to add an area() method for the Square class? Should
the area method be moved into the base Shape class and inherited by circle, square,
and rectangle? If so, what issues would result?'''

#as above I added area method to Rectangel class becouse the formula to ivaluate the area of circle and square are diffrent