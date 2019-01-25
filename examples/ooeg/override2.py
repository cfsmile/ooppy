class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('Aaaah...')
            self.hungry = False
        else:
            print('No thanks!')


class SongBird(Bird):
    def __init__(self):
        # slot for super init
        self.sound = 'Squawk!'
    def sing(self):
        print(self.sound)


b = Bird()
b.eat()  # didn't eat and hungry
b.eat()  # has eaten, not hungry

s = SongBird()
s.sing()
# s.eat()  # AttributeError

# super().__init__() #  do its job as if "by magic".

