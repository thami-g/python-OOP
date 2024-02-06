# DDD - Data Abstraction, Data Encapsulation, Data Hiding

class Robot:
    def __init__(self, name=None):
        self.name = name
    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am robot without a name")
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    
x = Robot()
x.set_name("Henry")
x.say_hi()
y = Robot()
y.set_name(x.get_name())
print(y.get_name())