# The usage of the __del__ method is very problematic. 
# If we change the previous code to  personalize the deletion of a robot,
# we create an error:

class Robot():
    def __init__(self, name):
        self.name = name
        print(name + " has been created!")
    def __del__(self):
        print(self.name + " says by-bye!")

if __name__ == "__main__":
    x = Robot("Tik-Tok")
    y = Robot("Jenkins")
    z = x
    print("Deleting x")
    del x
    print("Deleting z")
    del z
    del y
