class Robot:
    __counter = 0
    def __init__(self):
        type(self).__counter += 1
    def RobotInstances(self):
        return Robot.__counter

if __name__ == "__main__":
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    print(x.RobotInstances())
    Robot.RobotInstances() # this will produce an errror
    
    #This is not a good idea for two reasons: First of all, because the number of robots 
    # has nothing to do with a single robot instance and secondly because we can't inquire
    # the number of robots before we create an instance. If we try to invoke the method 
    # with the class name Robot.RobotInstances(), we get an error message, because it needs 
    # an instance as an argument: