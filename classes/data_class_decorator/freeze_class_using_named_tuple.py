from collections import namedtuple

ImmutableRobot = namedtuple("ImmutbaleRobot", ["name", "brandname"])

#  Example usage:
robot = ImmutableRobot(name="RoboX", brandname="TechBot")
print(robot.name)
print(robot.brandname)

# Attempting to modify attributes will raise an AttributeError
try:
    robot.name = "RoboY"
except AttributeError as e:
    print(e)

try:
    robot.brandname = "NewTechBot"
except AttributeError as e:
    print(e)