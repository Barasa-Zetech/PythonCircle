# Python program to getArea(to return area of a circle) and getCircumference(to return the circumference of the circle );

from math import pi
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def getArea(self):
        area = pi * (self.radius ** 2)
        return area
    def getCircumference(self):
        circumference = 2 * pi * self.radius
        return circumference
circle = Circle(5)
# Get the area of the circle
area = circle.getArea()
print("Area:", area)
# Get the circumference of the circle
circumference = circle.getCircumference()
print("Circumference:", circumference)
