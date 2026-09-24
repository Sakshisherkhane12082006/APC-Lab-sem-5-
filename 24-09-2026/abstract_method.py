from abc import ABC, abstractmethod
class Student(ABC):
    @abstractmethod
    def study(self):
        pass
class CollegeStudent(Student):
    def study(self):
        print("studying Python right now!!!")

s = CollegeStudent()
s.study()