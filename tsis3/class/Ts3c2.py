
class Shape():
    def area(self,area=0):
        self.area = area
        print(self.area)
        
class Square(Shape):
    def __init__(self,length):
        self.length = length
    def area(self,length):
        self.area = length**2
        print(self.area)
class Rectangle(Shape):
    def __init__(self,length1=0,width=0):
        self.length1 = length1
        self.width = width
    def area(self):
        self.area = self.length1 * self.width
        print(self.area)
    
sh = Shape()
sh.area()
sq = Square(4)
sq.area(4)
rc = Rectangle(3,4)
rc.area()
