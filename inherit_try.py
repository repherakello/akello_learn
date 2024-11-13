#Single inheritance instruction
class Rectangle:
    def calculate_area(x, y):
        print(2*(x * y))
    
class Area(Rectangle):
    pass

area1 = Area
area1.calculate_area(2,3)

#Multiple inheritance instruction
class Bird:
    def fly():
        print("This is an ostrich and its the largest bird!")

class Mammal:
    def run():
        print("Mammals are classified as warm blooded animals!")

class Bat(Bird,Mammal):
    pass

calling1 = Bat

calling1.fly()
calling1.run()


#Polymorphism with Duck typing instructions
class Dog:
    def make_sound():
        return "Who is shouting please?"
    
class Cat:
    def make_sound():
        print("It's jerry the chickey mouse.")

class Bird:
    def make_sound():
        print("He will face the consequences!")
# called1 = Dog()
# called2 = Cat()
# called3 = Bird()
def let_them_speak():
    coming = [Dog.make_sound(), Cat.make_sound(), Bird.make_sound()]

    print(coming)

let_them_speak()