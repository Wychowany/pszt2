import random
import Point


class Cargo:
    width = None
    height = None
    position = None
    inWarehouse = False
    id = None

    def __init__(self, cargo_type, id):
        self.width = cargo_type.width
        self.height = cargo_type.height
        self.id = id

    def randomize_position_of_left_corner(self):
        self.position = Point.Point(random.randrange(20, 80, 1), random.randrange(20, 80, 1))


class Square1x1:
    THIS_TYPE_NUMBER = 25
    width = 1
    height = 1


class Square2x2:
    THIS_TYPE_NUMBER = 90
    width = 2
    height = 2


class Square5x5:
    THIS_TYPE_NUMBER = 8
    width = 5
    height = 5


class Rectangle1x2:
    THIS_TYPE_NUMBER = 80
    width = 1
    height = 2


class Rectangle2x1:
    THIS_TYPE_NUMBER = 43
    width = 2
    height = 1


class Rectangle2x3:
    THIS_TYPE_NUMBER = 60
    width = 2
    height = 3


class Rectangle3x2:
    THIS_TYPE_NUMBER = 40
    width = 3
    height = 2
