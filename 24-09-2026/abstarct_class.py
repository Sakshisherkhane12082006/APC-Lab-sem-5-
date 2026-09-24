from abc import ABC
class Student(ABC):
    pass
class CollegeStudent(Student):
    def study(self):
        print("Student is studying")

s = CollegeStudent()
s.study()