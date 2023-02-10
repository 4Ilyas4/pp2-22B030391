import math as m
class point:
    def __init__(self,x,y,x1=0,y1=0):    
        self.distc = 0
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
    def show(self):
        print(self.x,self.y)
    def move(self,x1,y1):
        self.x = x1
        self.y = y1
    def dist(self,x2,y2):
        self.distc = m.sqrt(((self.x1-self.x)**2)+((self.y1-self.y)**2))
        print(self.distc)

p = point(1,1)
p.show()
p.move(2,3)
p.show()
p.dist(4,4)
