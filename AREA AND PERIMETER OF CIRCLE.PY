import math
class circle:

    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return math.pi * self.radius **2
    
    def perimeter(self):
        return 2* math.pi *self.radius

r=float(input("Enter the radius:"))

c=circle(r)
print("Area:",c.area())
print("perimeter:",c.perimeter())