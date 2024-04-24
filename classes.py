class Test:
    x = 5


obj = Test()
print(obj.x)


class Test2:
    x = 10

    def testing_world(self):
        print("This is testing world")
        print(self.x)


obj = Test2()
print(obj.testing_world())


class Test3:
    x = 1234
    b = 1234

    def add(self):
        return self.x + self.b

    def diff(self):
        return self.x - self.b

    def calc(self):
        return self.add(), self.diff()


obj = Test3()
print(obj.calc())


class Test4:
    def __init__(self):
        self.a = 22
        self.b = 44
        print(self.a, self.b)


obj = Test4()


class Test5:
    def __init__(self, a):
        self.data = 1
        self.test = 2

    def testing(self):
        return f"This is function {self.data} "


a = input("Enter a number: ")
obj = Test5()
print(obj.testing())
