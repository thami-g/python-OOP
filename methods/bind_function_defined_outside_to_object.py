def hi(obj):
    print("Hi, I am " + obj.name + "!")
    

class Robot:
    # binding happens here
    say_hi = hi

x = Robot()
x.name = "Marvin"
hi(x)

Robot.say_hi(x)
x.say_hi()