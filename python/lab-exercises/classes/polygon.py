""" Polygons App """

# Import the Abstract Base Class:
from abc import abstractmethod

class Polygon:

    """ # Create class and sub-class objects which represent different geometrical shapes """

    def __init__(self, passedheight, passedwidth):
        self.height = passedheight
        self.width = passedwidth

    @abstractmethod
    def area(self, shape=None):
        """ This method will be inherited """

    @abstractmethod
    def perimeter(self, shape=None):
        """ This method will be inherited """

class GeometricShapes(Polygon):

    """ Work out area and perimeter, inheriting attirbutes and methods from the Polygon class """

    def area(self, shape):
        """ Inherited from Polygon class """
        area_calculation = self.width * self.height
        return "Area of the {} is {}".format(shape, area_calculation)

    def perimeter(self, shape):
        """ Inherited from Polygon class """
        perimeter_calculation = 2 * (self.height + self.width)
        return "Perimeter of the {} is {}".format(shape, perimeter_calculation)

square = GeometricShapes(10, 5)
print(square.area("square"))
print(square.perimeter("square"))

rectangle = GeometricShapes(15, 10)
print(rectangle.area("rectangle"))
print(rectangle.perimeter("rectangle"))
