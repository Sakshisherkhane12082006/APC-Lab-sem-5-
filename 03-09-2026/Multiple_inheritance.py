class P1:
    def show_P1(self):
        print("Parent class 1")
class P2:
    def show_P2(self):
        print("Parent class 2")
class P3:
    def show_P3(self):
        print('Parent class 3')
        
class Child(P1,P2,P3):
    pass

c=Child()
c.show_P1()
c.show_P2()
c.show_P3()