class Pet:
    _class_info = "pet animals"
    @staticmethod
    def about():
        print("This class is about " + Pet._class_info + "!")

class Dog(Pet):
    _class_info = "man's best friends"

class Cat(Pet):
    _class_info = 'all kinds of cats'

Pet.about()
Dog.about()
Cat.about()