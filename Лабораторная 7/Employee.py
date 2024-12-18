class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def get_info(self):
        return self.name, self.id
class Manager(Employee):
    def __init__(self, name, id, departament):
        Employee.__init__(self, name, id)
        self.departament = departament
    def manage_project(self):
        return self.name, self.id, self.departament
class Technician(Employee):
    def __init__(self, name, id, specialization):
        Employee.__init__(self, name, id)
        self.specialization = specialization
    def perform_maintenance(self):
         return self.name, self.id, self.specialization
class TechManager(Manager, Technician):
    def __init__(self, name, id, departament, specialization):
        Manager.__init__(self, name, id, departament)
        Technician.__init__(self, name, id, specialization)
    def add_employee(self, new_sotr):
        self.name = new_sotr
    def  get_team_info(self):
        return self.name, self.id, self.departament, self.specialization
Sotr1 = Employee('Iman', 1)
Sotr2 = Manager('Kolya', 2, 'IT')
Sotr3 = Technician('Misha', 3, 'Tester')
Sotr4 = TechManager('Egor', 4, 'IT', 'Tester')
print(Sotr1.get_info())
print(Sotr2.manage_project())
print(Sotr3.perform_maintenance())
print(Sotr4.get_team_info())


