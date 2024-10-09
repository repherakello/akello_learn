import math
class circle:
    def __init__(self, radius):
        self.radius = radius

    def getPerimeter(self):
        return 2 * self.radius * math.pi
    
    def getArea(self):
        return 2 *math.pi ** self.radius
    
    def setRdius(self,radius):
        self.radius = radius

Area1 = circle(2)
perimeter1 = circle(20)

print(f"The are of a circle of radius {Area1.radius} is: {Area1.getArea()}")
print(f"The perimeter of a circle of radius {perimeter1.radius} is, {perimeter1.getPerimeter()}")