class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type
    def get_info(self):
        return self.make, self.model, self.fuel_type
mka = Car('Bmw', '5-s', 98)
print(mka.get_info())