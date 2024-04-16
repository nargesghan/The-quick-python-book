'''Write a class method similar to total_area() that returns the total circumference of
all circles.'''

'''"""circle_cm module: contains the Circle class."""
class Circle:
"""Circle class"""
all_circles = [] 1
pi = 3.14159
def __init__(self, r=1):
"""Create a Circle with the given radius"""
self.radius = r
self.__class__.all_circles.append(self)
def area(self):
"""determine the area of the Circle"""
return self.__class__.pi * self.radius * self.radius
@classmethod 2
def total_area(cls): 3
total = 0
for c in cls.all_circles: 4
total = total + c.area()
return total
>>> import circle_cm
>>> c1 = circle_cm.Circle(1)
>>> c2 = circle_cm.Circle(2)
>>> circle_cm.Circle.total_area()
15.70795
>>> c2.radius = 3
>>> circle_cm.Circle.total_area()
31.415899999999997
'''

class Circle:
    """Circle class"""
    all_circles=[]
    pi=3.14159
    
    def __init__(self,r=1):
        """Create a circle with the given radius"""
        sefl.radius=r
        self.__class__.all_circles.append(self)

    def area(self):
        """determine the area of the circle"""
        return self.__class__.pi*self.radius*self.radius
    
    def circumference(self):
        """determine the circumference of the circle"""
        return 2*self.__class__.pi*self.radius
    
    @classmethod
    def total_area(cls):
        total=0
        for circle in cls.all_circles:
            total=total+circle.area()
        return total
    
    @classmethod
    def total_circumference(cls):
        total=0
        for circle in cls.all_circles:
            total=total+circle.circumference()
        return total
