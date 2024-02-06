class Robot:
    def __init__(self, name=None, build_year=2000):
        self.__name = name
        self.__build_year = build_year

    def say_hi(self):
        if self.__name:
            print(f"Hi, I am {self.__name}")
        else:
            print("Hi, I am robot without a name")

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_build_year(self, by):
        self.__build_year = by

    def get_build_year(self):
        return self.__build_year

    def __repr__(self):
        return f"Robot('{self.__name}', '{self.__build_year}')"

    def __str__(self):
        return f"Name: {self.__name} , Build Year: {self.__build_year}"


if __name__ == "__main__":
    x = Robot("Marvin", 1979)
    y = Robot("Caliban", 1943)
    for rob in [x, y]:
        rob.say_hi()
        if rob.get_name() == "Caliban":
            rob.set_build_year(1993)
        print(f"I was built in the year { str(rob.get_build_year())} !")
