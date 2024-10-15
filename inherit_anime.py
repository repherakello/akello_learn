class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Title:
    def __init__(self, title):
        self.title = title

class Combine(Human, Title):
    def __init__(self, name, age, title):
        Human.__init__(self, name, age)
        Title.__init__(self, title)

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Title: {self.title}")

# Example usage
combine_instance = Combine("Repher", 20, "Developer")
combine_instance.display_info()



#Multilevel inheritance:
"""A child class inherits from a parent class in which also had inherited from another parent class."""

class Vehicle:
    def move(self):
        print("Moving")

class Car(Vehicle):
    pass

class ElectricCar(Car):
    def charge(self):
        print("Charging")

tesla = ElectricCar()
tesla.move()
tesla.charge()