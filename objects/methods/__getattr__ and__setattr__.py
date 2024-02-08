# class Robot:
#     def __init__(self, name, build_year, city):
#         self.name = name
#         self.build_year = build_year
#         self.city = city
        
#     @property
#     def name(self):
#         return self.__name
    
#     @property
#     def build_year(self):
#         return self.__build_year
    
#     @property
#     def city(self):
#         return self.__city
    
#     @name.setter
#     def name(self, value):
#         self.__name = value
        
#     @build_year.setter
#     def build_year(self, value):
#         self.__build_year = value
    
#     @city.setter
#     def city(self, value):
#         self.__city = value
        

# Example usage:

# robot = Robot("RobotBot", 2022, "TechCity")
# print(robot.name)
# print(robot.build_year)


# -------------------------------------------------------------------------------------------------------------
#                       Refactored version using generic getters and setter
# from typing import Any


# class Robot:
#     def __init__(self, name, build_year, city):
#         self.name = name
#         self.build_year = build_year
#         self.city = city
        
#     def __getattr__(self,name):
#         return self.__dict__[f"__{name}"]
    
#     def __setattr__(self,name, value):
#         self.__dict__[f'__{name}'] = value
        
# robot = Robot("RobotBot", 2022, "TechCity")

# print(robot.name)
# print(robot.build_year)
# print(robot.city)
# -------------------------------------------------------------------------------------------------------------
#                              attributes have some conditions to fulfill.

class Robot:
    def __init__(self,name,build_year,city):
        self.name = name
        self.build_year = build_year
        self.city = city
        
    def __getattr__(self, name):
        return self.__dict__[f"__{name}"]
    
    def __setattr__(self, name, value):
        if name == 'name':
            if value in ['Henry', 'Oscar']:
                raise ValueError('Not a decent Robot name')
        elif name == 'build_year':
            if int(value) < 2020:
                raise ValueError('Build Year has to be after 2019')
        self.__dict__[f"__{name}"] = value

robot = Robot("Marvin", 2020, "TechCity")

print(robot.name)
print(robot.build_year)
print(robot.city)
    