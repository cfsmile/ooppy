# *** polymorphism demo 1 ***


class Animal:
    def __init__(self, name):    # Constructor
        self.name = name

    def talk(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Cat(Animal):
    def talk(self):
        return 'Meow!'


class Dog(Animal):
    def talk(self):
        return 'Woof! Woof!'


animals = [Cat('Missy'),
           Cat('Mr. Mistoffelees'),
           Dog('Lassie')]

for animal in animals:
    """python automatically decide which subclass does an animal belong.
    And do the corresponding behavior."""
    print(animal.name + ': ' + animal.talk())

# Missy: Meow!
# Mr. Mistoffelees: Meow!
# Lassie: Woof! Woof!

# *** polymorphism demo2 ***


class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def whoAmI(self):
        return 'I am a Person, my name is %s' % self.name


class Student(Person):
    def __init__(self, name, gender, score):
        super().__init__(name, gender)
        self.score = score

    def whoAmI(self):
        return 'I am a Student, my name is %s' % self.name


class Teacher(Person):
    def __init__(self, name, gender, course):
        super().__init__(name, gender)
        self.course = course

    def whoAmI(self):
        return 'I am a Teacher, my name is %s' % self.name


def who_am_i(x):
    """Another style. This function is like a factory.
    It produce various objects. These object could properly
    do their jobs ."""
    print(x.whoAmI())


p = Person('Tim', 'Male')
s = Student('Bob', 'Male', 88)
t = Teacher('Alice', 'Female', 'English')

who_am_i(p)
who_am_i(s)
who_am_i(t)
