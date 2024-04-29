class Test1:
    a = "Test"


class Test2(Test1):
    b = "Hello"


obj = Test2()
print(obj.b)
print(obj.a)

class Parent():
    a = 10 
    b = 11

    def add(self):
        return self.a + self.b
class Child(Parent):
    def diff(self):
        return self.a - self.b
    def calc(self):
        return self.add(), self.diff()
obj= Child()