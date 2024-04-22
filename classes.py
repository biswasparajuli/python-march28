class Test:
    x = 5


obj = Test()
print(obj.x)

class Test2():
    x = 10
    def testing_world(self):
        print('This is testing world')
        print(self.x)
        
obj = Test2()
print(obj.testing_world())
