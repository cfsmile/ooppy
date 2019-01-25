
class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self):    #  构造函数
        """ Create a new point at the origin """
        self.x = 1
        self.y = 1

    def reset(self):
        self.x = 0
        self.y = 0

p = Point()  # 创建一个对象p，也称实例化initialization
q = Point()

print(p.x, p.y, q,x, q.y)

p.reset()
print(p.x, p.y, q.x, q.y)


Point.reset(q)
print(q.x, q.y)

# 如果
class Point2:
    def reset():
        pass

z = Point()
z.reset()  # TypeError
#+end_src


#+begin_src python :results output
  import math

  class Point:
      """ Represents a point in two-dimensional geometric coordinates. """

      def __init__(self):    #  构造函数
          """Initialize the position of a new point. The x and y coords can be
  specified. If they are not, the point default to the (1,1)."""
          self.x = 1
          self.y = 1   # Any idea? In the programming world, duplicate
                       # code is considered evil.

  #    def __init__(self, x=1, y=1):
  #        self.move(x, y)

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

  # 使用
  p1 = Point()
  p2 = Point()

  p1.reset()
  p2.move(5, 0)

  print(p2.calculate_distance(p1))

  assert (p2.calculate_distance(p1) == p1.calculate_distance(p2))

  p1.move(3, 4)
  print(p1.calculate_distance(p2))
  print(p1.calculate_distance(p1))
#+end_src
