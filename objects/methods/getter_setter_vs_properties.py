class Circle:
    def __init__(self, radius):
        self._radius = radius
        
    def get_area(self):
        return 3.14 * self._radius**2

    def set_area(self, value):
        if value < 0:
            raise ValueError("Radius must be non-negative")
        self._radius = value