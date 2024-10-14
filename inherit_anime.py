class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Generic animal sound:")

class Dog(Animal):
    def make_sound(self):
        return "Woof!"
    
dog1 = Dog("Pracks")
dog1.make_sound()