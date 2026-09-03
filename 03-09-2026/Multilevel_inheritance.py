class class1:
    def display1(self):
        print("Class 1")
class class2(class1):
    def display2(self):
        print("class 2")
class class3(class2):
    pass
c=class3()
c.display1()
c.display2()