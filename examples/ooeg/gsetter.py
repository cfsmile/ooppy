# coding: utf-8
#!/usr/bin/env python


class Robot:

    def __init__(self, name=None, build_year=None):
        self._name = name
        self._build_year = build_year

    def say_hi(self):
        if self._name:
            print("Hi, I am " + self._name)
        else:
            print("Hi, I am a robot without a name")
        if self._build_year:
            print("I was built in " + str(self._build_year))
        else:
            print("It's not known, when I was created!")

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_build_year(self, by):
        self._build_year = by

    def get_build_year(self):
        return self._build_year

    # learn __repr__ and __str__ by yourself
    def __repr__(self):

        return "Robot('" + self._name + "\'," + str(self._build_year) + ")"

    def __str__(self):
        return "Name:" + self._name + ", Build Year: " + str(self._build_year)


x = Robot("Henry", 201)
y = Robot()
y.set_name("Marvin")
x.say_hi()
y.say_hi()
print(str(x))
print(str(y))
