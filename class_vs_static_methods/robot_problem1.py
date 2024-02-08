class Pet:
    _class_info = "pet animals"
    def about(self):
        print("This class is about " + self._class_info + "!")

class Dog(Pet):
    _class_info = "man's best friend"

class Cat(Pet):
    _class_info = "All kinds of cats"

p = Pet()
p.about()
d = Dog()
d.about()
c = Cat()
c.about()