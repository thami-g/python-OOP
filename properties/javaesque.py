class P:
    def __init__(self, x):
        self.__x = x
        
    def get_x(self):
        return self.__x
    
    def set_x(self, x):
        self.__x = x

p1 = P(42)
p2 = P(4711)
print(p1.get_x())
        
    
    