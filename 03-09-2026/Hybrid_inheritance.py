class Parent:
    def show_parent(self):
        print("Parent class")
class C1(Parent):
    def show_child1(self):
        print("Child 1")
class C2(Parent):
    def show_child2(self):
        print("Child 2")
class Child3(C1, C2):
    pass


c = Child3()

c.show_parent()
c.show_child1()
c.show_child2()