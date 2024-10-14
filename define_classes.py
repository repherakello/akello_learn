"""
In this program i will be creating and using classes 
"""

#Defining a simple class
class Name:
    def __init__(self,call:str = "akello"):
        self.call = call

    def calling(self):
        name =input("What is your name:")
        if name == "akello":
            return f"interesting {name}"
    
    def named(self,name):
        self.name = name

pass

# Accessing members of a class:
c1 =Name
print("My name is",c1.named)