class Father:
    __private = 10
    _protected = 20
    def show(self):
        print("Father class")

class Son(Father):
    def show_protected(self):
        print("Protected:", self._protected)

class Grandson(Son):
    def show_value(self):
        print("Protected:", self._protected)


g = Grandson()

g.show()
g.show_protected()
g.show_value()