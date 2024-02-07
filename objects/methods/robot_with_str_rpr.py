class Robot:
    def __init__(self,name,build_year):
        self.name = name
        self.build_year = build_year
    def __str__(self):
        return f"Name: {self.name} , Build Year: {self.build_year}"
    def __repr__(self):
        return f"Robot('{self.name}','{self.build_year}')"
    
    
if __name__ == "__main__":
    x = Robot("Marvin", 1979)
    x_repr = repr(x)
    print(x_repr)
    print("Type of x_repr: ", type(x_repr))
    new = eval(x_repr)
    print(new)
    print("Type of new:", type(new))
        