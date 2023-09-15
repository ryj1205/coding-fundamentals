# Import the Abstract Base Class
from abc import ABC, abstractmethod

##################################################################
# Goal:
# Create class and sub-class objects which represent different geometrical shapes, such as Rectangles and Squares
# objects should have methods to display area and perimeter
##################################################################

class Polygon:

    def __init__(self, passedheight, passedwidth):
        self.height = passedheight
        self.width = passedwidth

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

##################################################################

class GeometricShapes(Polygon):

    def area(self):
        area_calculation = self.width * self.height
        return area_calculation

    def perimeter(self):
        perimeter_calculation = 2 * (self.height + self.width)
        return perimeter_calculation

##################################################################

square = GeometricShapes(10, 5)
print(square.area())
print(square.perimeter())

rectangle = GeometricShapes(15, 10)
print(rectangle.area())
print(rectangle.perimeter())

##################################################################