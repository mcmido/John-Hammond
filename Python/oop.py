# Object Orientated Programing

# class dog:
#     def __init__(self, name, age, number):
#         self.name = name
#         self.age = age
#         self.number = number
#
#
#     def bark(self):
#         print("WOOF WOOF!!")
#
#     def add_one(self, x):
#         print(x + 1)
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#     def get_number(self):
#         return self.number
#
# a = dog("ahmed", 15, 20118078453)
# print(a.get_age ())
# print(a.get_number())
# type(a.get_number())
#
#
#
#
#
#
#
# class screen:
#     def __init__(self, size):
#         self.size = size
#
#     def get_size(self):
#         return self.size
# a = screen(2500)
# print(a.get_size())
# Class Named Dog
# class Dog:
# # Function inside the Class of Dog
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print(name)
#
#     def get_age(self):
#         return self.age
#
#     def set_age(self, age):
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def bark(self):
#         print("WOOF WOOF")
#
#     def size(self, x):
#         return x + 1
#
#
# dog1_name = "tim"
# dog1_age = 34
#
# dogs_name = ["tim", "Bill"]
# dogs_age = [14, 15, 16, 18]

# More Complex Example...
# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade # 0 - 100
#
#
#     def get_grade(self):
#         return self.grade
#
#
# class Course:
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []
#
#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False
#
#     def get_average_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()
#
#         return value / len(self.students)
#
# s1 = Student("Tim", 19, 95)
# s2 = Student("Bill", 19, 75)
# s3 = Student("Jill", 19, 65)
#
# course = Course("Science", 2)
# course.add_student(s1)
# course.add_student(s2)
# print(course.get_average_grade())



class Students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0 - 100

    def get_grade(self):
        return self.grade

class Cources:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []


    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
            print(value)
        return value / len(self.students)


s1 = Students("Tim", 19, 95)
s2 = Students("Bill", 19, 75)
s3 = Students("Jill", 19, 65)

course = Cources("Science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.get_average_grade())
