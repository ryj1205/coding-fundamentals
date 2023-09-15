# Import the Abstract Base Class:
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

class Square(Polygon):

    def area(self):
        area_calculation = self.width * self.height
        return "Area of the square is {}".format(area_calculation)

    def perimeter(self):
        perimeter_calculation = 2 * (self.height + self.width)
        return "Perimeter of the square is {}".format(perimeter_calculation)

class Rectangle(Polygon):

    def area(self):
        area_calculation = self.width * self.height
        return "Area of the rectangle is {}".format(area_calculation)

    def perimeter(self):
        perimeter_calculation = 2 * (self.height + self.width)
        return "Perimeter of the rectangle is {}".format(perimeter_calculation)

##################################################################

square_obj = Square(10, 5)
print(square_obj.area())
print(square_obj.perimeter())
print("")

rectangle_obj = Rectangle(15, 10)
print(rectangle_obj.area())
print(rectangle_obj.perimeter())
print("")

##################################################################
##################################################################
##################################################################

class GeometricShapes(Polygon):

    def area(self, shape):
        area_calculation = self.width * self.height
        return "Area of the {} is {}".format(shape, area_calculation)

    def perimeter(self, shape):
        perimeter_calculation = 2 * (self.height + self.width)
        return "Perimeter of the {} is {}".format(shape, perimeter_calculation)

##################################################################

square = GeometricShapes(10, 5)
print(square.area("square"))
print(square.perimeter("square"))
print("")

rectangle = GeometricShapes(15, 10)
print(rectangle.area("rectangle"))
print(rectangle.perimeter("rectangle"))

##################################################################