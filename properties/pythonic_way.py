class P:
    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
p1 = P(1001)
print(p1.x)

p1.x = -12
print(p1.x)
# There is still another problem in this version.
# We have now two ways to access or change the value of x: Either
# by using "p1.x = 42" or by "p1.set_x(42)". This way we are violating
# one of the fundamentals of Python: "There should be one-- and 
# preferably only one --obvious way to do it." 