from math import sqrt, atan2
''' classes utiles '''


class Vector():
    """Create a Vector."""

    def __init__(self, a, b):
        self.x = a
        self.y = b

    def norm(self):
        return sqrt( (self.x*self.x) + (self.y*self.y) )

    def angle(self):
        return atan2(self.y, self.x)




class Point():
    def __init__(self, a, b):
        self.x = a
        self.y = b
