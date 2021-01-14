# coding: utf-8
#!/usr/bin/env python


import math


class Point:
    """ Represents a point in two-dimensional geometric coordinates. """

    def __init__(self):
        """Initialize the position of a new point. The x and y coords can be
  specified. If they are not, the point default to the (1,1)."""
        self.x = 1
        self.y = 1

    def move(self, x, y):
        """Move the point to a new location in 2D space."""
        self.x = x
        self.y = y

    def reset(self):
        """ Reset the point back to the origin(0,0)"""
        self.move(0, 0)

    def calculate_distance(self, other_point):
        """Calculate the distance from this point to a second point passed as
  aparameter."""
        return math.sqrt(
            (self.x - other_point.x) ** 2 +
            (self.y - other_point.y) ** 2)


# useage
p1 = Point()
p2 = Point()

p1.reset()
p2.move(5, 0)

print(p2.calculate_distance(p1))

assert (p2.calculate_distance(p1) == p1.calculate_distance(p2))

p1.move(3, 4)
print(p1.calculate_distance(p2))
print(p1.calculate_distance(p1))

# Any idea to polish the code?
# In the programming world, duplicate code is considered evil.
# Is the second version __init__ better than the previous?
#    def __init__(self, x=1, y=1):
#        self.move(x, y)
