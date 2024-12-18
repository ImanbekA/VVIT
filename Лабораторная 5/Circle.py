class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def set_radius(self, new_radius):
        self.radius = new_radius
circ = Circle(3)
print(circ.get_radius())
circ.set_radius(4)
print(circ.get_radius())
