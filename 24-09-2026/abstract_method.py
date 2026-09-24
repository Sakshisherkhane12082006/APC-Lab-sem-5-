from abc import ABC, abstractmethod
class Student(ABC):
    @abstractmethod
    def study(self):
        pass
class CollegeStudent(Student):
    def study(self):
        print("I am studying Python")

s = CollegeStudent()
s.study()