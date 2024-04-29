class Parent:
    def __init__(self):
        self.a = 10
        self.b = 11

    def add(self):
        return self.a
        


class Child(Parent):
    def __init__(self):
        self.c = 0
        self.d = 11
        Parent.__init__(self)

    def sub(self):
        return self.add()


obj = Child()
print(obj.sub())


class Parent1():
    def __init__(self):
        self.a = 10
        self.b = 11

    def add(self):
        return self.a
        
class Parent2():
    def __init__(self):
        self.a = 14
        self.b = 16

    def sub(self):
        return self.b

class Child(Parent1, Parent2):
    def __init__(self):
        self.e = 0
        self.f = 11
        Parent1.__init__(self)
        Parent2.__init__(self)

    def prd(self):
        return self.add(), self.sub()


obj = Child()
print(obj.prd())