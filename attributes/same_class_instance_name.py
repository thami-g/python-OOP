class Robot():
    pass

x = Robot()
Robot.brand = "Kuka"
print(x.brand)

x.brand = "Thales"
print(Robot.brand)

y = Robot()
print(y.brand)

Robot.brand = "Thales"
print(y.brand)

print("x: ",x.__dict__)
print("y: ",y.__dict__)
print("Robot: ",Robot.__dict__)
# print(x.energy) error

# prevents error above
print(getattr(x,"energy", 100))