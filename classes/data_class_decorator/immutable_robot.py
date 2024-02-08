from dataclasses import dataclass


@dataclass(frozen=True)
class ImmutableRobot:
    name: str
    brandname: str


# Example usage:
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

try:
    robot.city = "Hamburg"
except AttributeError as e:
    print(e)