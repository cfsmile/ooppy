#! /usr/bin/env python
# -*- coding: utf-8 -*-

####
# Implementation using data structure and functions
####

import math

#  Data Structure part
# Each polygon is represented as a list of points
# The points are modeled as two-tuples(x,y) describing where
# that point is located.
square = [(1, 1), (1, 2), (2, 2), (2, 1)]

#  Functions part

def distance(p1, p2):
    """"""
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def perimeter(polygon):
    pmeter = 0
    points = polygon + [polygon[0]]
    # square + [square[0]]
    # [(1, 1), (1, 2), (2, 2), (2, 1), (1, 1)]
    # made a circle to calculate sum of edges as perimeter
    for i in range(len(polygon)):
        pmeter += distance(points[i], points[i+1])

    return pmeter

# >>> square = [(1,1), (1,2), (2,2), (2,1)]
# >>> perimeter(square)
# 4.0


####
# Implementation using class fashion
####

import math

class Point:
    """"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p2):
        """"""
        return math.sqrt((self.x-p2.x)**2 + (self.y-p2.y)**2)
class Polygon:
    """"""
    def __init__(self):
        """"""
        self.vertices = []

    def add_point(self, point):
        """"""
        self.vertices.append((point)) # elements of the list is tuple

    def perimeter(self):
        """"""
        pmeter = 0
        points = self.vertices + [self.vertices[0]]

        for i in range(len(self.vertices)):
            pmeter += points[i].distance(points[i+1])

        return pmeter


# fred@TPW:~/dlmu_notes/Curriculum/ooppy/py$ python -i polygons.py
# >>> s = Polygon()
# >>> s.add_point(Point(1,1))
# >>> s.add_point(Point(1,2))
# >>> s.add_point(Point(2,2))
# >>> s.add_point(Point(2,1))
# >>> s.perimeter
# <bound method Polygon.perimeter of <__main__.Polygon instance at 0x7f08390cc950>>
# >>> s.perimeter()
# 4.0


# Readability, easy to read.
