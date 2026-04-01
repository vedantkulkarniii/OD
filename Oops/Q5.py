# *5. Learning Management System *
# 📌 Question:
# Design a learning management system:  Create a class hierarchy where Person is the base class, and Student and Teacher are derived classes. Demonstrate how inheritance allows different attributes and behaviors for students and teachers.

# 📖 Explanation:
# Inheritance allows reuse and specialization

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def role(self):
        print(self.name, "is Student")

class Teacher(Person):
    def role(self):
        print(self.name, "is Teacher")

Student("Ram").role()
Teacher("Sir").role()