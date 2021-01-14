# coding: utf-8
#!/usr/bin/env python


class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def setSize(self, size=(0, 0)):
        self.width, self.height = size

    def getSize(self):
        return self.width, self.height

    size = property(getSize, setSize)  # old syntax


# use setter and getter
r = Rectangle()
r.width = 10
r.height = 5
r.getSize()
r.setSize((150, 100))
r.width

# use property
r = Rectangle()
r.width = 10
r.height = 5
r.size
r.size = 150, 100
r.width
