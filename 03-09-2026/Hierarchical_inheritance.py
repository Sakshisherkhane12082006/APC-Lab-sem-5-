class Parent:
    def show(self):
        print("parent class")
class Child1(Parent):
    pass
class Child2(Parent):
    pass
c1=Child1()
c2=Child2()
c1.show()
c2.show()