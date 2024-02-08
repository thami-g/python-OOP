# class ImmutableRobot:
#     def __init__(self, name, brandname):
#         self.__name = name
#         self.__brandname = brandname

#     def get_name(self):
#         return self.__name

#     def get_brandname(self):
#         return self.__brandname

# robot = ImmutableRobot(name="RoboX", brandname="TechBot")
# print(robot.get_name())
# print(robot.get_brandname())


# We can rewrite the previous example by using properties and not suppling the setter methods.
# So logically the same as before:


class ImmutableRobot:
    def __init__(self, name, brandname):
        self.__name = name
        self.__brandname = brandname

    @property
    def name(self):
        return self.__name

    @property
    def brandname(self):
        return self.__brandname


robot = ImmutableRobot(name="RoboX", brandname="TechBot")
print(robot.name)
print(robot.brandname)

try:
    robot.name = "RoboY"
except AttributeError as e:
    print(e)


try:
    robot.brandname = "NewTechBot"
except AttributeError as e:
    print(e)
