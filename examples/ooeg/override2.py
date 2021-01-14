# coding: utf-8
#!/usr/bin/env python

"""A example override."""


class Person():
    """Super class Person"""
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def __str__(self):
        return self.firstname + " " + self.lastname


class Teacher(Person):
    """Subclass Teacher"""
    def __init__(self, first, last, major):
        super().__init__(first, last)
        self.major = major

    def __str__(self):
        """Retrun name and major."""
        return super().__str__() + ", " + self.major


class Student(Person):
    """Subclass Student"""
    def __init__(self, first, last, stu_num):
        super().__init__(first, last)
        self.stu_num = stu_num

    def __str__(self):
        """Return name and student number."""
        return super().__str__() + ", " + self.stu_num


a = Person("Michael", "Jordan")
b = Student('Kobe', 'Bryant', "1001")
c = Teacher('LeBron', 'James', 'Computer Science')

print(a)
print(b)
print(c)
