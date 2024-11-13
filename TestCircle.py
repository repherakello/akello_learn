#ENCAPSULATION:
class Student: #Class is a blue print for creating object
    age = 22
    def __init__(self,name,grade, age):
        self.name = name #Public attribute
        self.__grade = grade #private attribute(encapsulation)
        self.age = age

        def __str__(self):
            return f"name is {self.name} age is {self.age} with the grade {self.__grade}"
    
    #Public method to enroll student
    def enroll(self):
        print(f"{self.name} has been enrolled")



    #   Public method to view students grade
    def view_grade(self):
        print(f"{self.name}'s grade is: {self.__grade} whose age is {self.age}")


#Creating an instance of student
student1 = Student("Akello", "C Plain",22)
student2 = Student("Repher", "A",23)

print(student1._Student__grade) #How to access private attribute! 
print(student2.name)  

student2.view_grade() #object
student1.enroll() #object
student1.view_grade()

#trying the class import from classes_1

# from classes_1 import circle

# def main():
#     circle1 = circle()
#     print("The area of the circle of radius",circle1.radius, "is", circle1.getArea())


#     circle2 = circle(14)
#     print("The area of the circle whose radius", circle2.radius, "is", circle2.getArea())

# main()