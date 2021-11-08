#OOP

#object
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def get_name(self):
#         return self.name

#     def get_age(self):
#         return self.age
#     def set_age(self, age):
#         self.age = age


# class Student:
#     def __init__ (self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def get_grade(self):

#         class Course:
#             def __init__(self, name, max_students):
#                 self.name = name
#                 self.max_students = max_students   
#                 self.students = []
#                 self.is_active = False

#             def add_student(self, student):
#                 if len(self.students) < self.max_students:
#                     self.students.append(student)
#                     return True
#                 return False

#             def get_average_grade(self):
#                 value = 0
#                 for student in self.students:
#                     value += student.get_grade()
                
#                 return value / len(self.students)

# s1 = Student("Tim", 19, 95)
# s2 = Student("Bill", 19, 74)
# s3 = Student("Jill", 19, 65)

# course = Course("Science", 2)
# course.add_student(s1)
# course.add_student(s2)
# print(course.students[0].name)
class Pet:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")
       
class Dog(Pet):
    def speak(self):
        print("Bark")


p = Pet("Tim", 19)
p.show()
c = Cat("Bill", 34, "Orange")
c.show()