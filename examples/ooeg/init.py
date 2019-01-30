# coding: utf-8
#!/usr/bin/env python


class Robot:
    """A Robot class"""
    def __init__(self, name=None):

        print("__init__ has been executed!")
        self.name = name

    def __del__(self):
        """Deconstructor is rarely used"""
        print("Robot has been destroyed")

    def say_hi(self):

        if self.name:
            print("Hi, I am" + self.name)
        else:
            print("Hi, I am a robot without a name.")


x = Robot()
x.say_hi()

y = Robot("Marvin")
y.say_hi()

print("Deleting x")
del x
print("Deleting y")
del y
