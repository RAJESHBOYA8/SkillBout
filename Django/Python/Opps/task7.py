class Animal:
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print('Dog')
class Cat(Animal):
    def make_sound(self):
        print('Cat')
for i in [Dog(),Cat()]:
    i.make_sound()