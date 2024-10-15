class A:
    def greet(self):
        return "Hello from class A"
    
class B(A):
    def greet(self):
        return "Hello from class B"
    
class C(A):
    def greet(self):
        return "Hello from class C"
    
class D(C,B):   #trying changing the postion of the arguments to see output
    pass

#creating an instance of class D

obj_d = D()
print(obj_d.greet())