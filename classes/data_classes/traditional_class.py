from dataclasses import dataclass


class Robot_traditional:
    
    def __init__(self, model, serial_number, manufacturer):
        self.model = model
        self.serial_number = serial_number
        self.manufacturer = manufacturer
        
# Here, the dataclass decorator automates the generation of special methods like __init__, 
# reducing the need for boilerplate code. The class definition is concise, making it 
# clearer and more maintainable, especially as the number of attributes increases.

@dataclass
class Robot:
    model: str
    serial_number: str
    manufacturer: str

x = Robot_traditional("NanoGuardian XR-2000", "234-76", "Cyber Robotics Co.")
y = Robot("MachinaMaster MM-42", "986-42", "Quantum Automations Inc.")

print(repr(x))
print(repr(y)) # uses __repr__tr