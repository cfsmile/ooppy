# coding: utf-8
#!/usr/bin/env python

"""A example of single inheritance."""


class Person():
    """Super class Person"""
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        """Return full name"""
        return self.firstname + " " + self.lastname


class Teacher(Person):
    """Subclass Teacher"""
    def __init__(self, first, last, major):
        Person.__init__(self, first, last)
        self.major = major

    def get_tchr(self):
        """Retrun name and major."""
        return self.Name() + ", who is major in " + self.major


class Student(Person):
    """Subclass Student"""
    def __init__(self, first, last, stu_num):
        Person.__init__(self, first, last)
        self.stu_num = stu_num

    def get_stu(self):
        """Return name and student number."""
        return self.Name() + "," + self.stu_num


a = Person("Michael", "Jordan")
b = Student('Kobe', 'Bryant', "1001")
c = Teacher('LeBron', 'James', 'Computer Science')

print(a.Name())
print(b.Name())
print(c.Name())

# print(a.get_stu())  # error
print(b.get_stu())
# print(c.get_stu())  # error
print(c.get_tchr())
