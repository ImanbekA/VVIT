class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    def get_info(self):
        return self.username, self.email, self.password
    def set_password(self, new_password):
        self.password = new_password
    def check_password(self, check):
        if self.password == check:
            return True
        else:
            return False

Kolya = UserAccount('Kolya', 'Kolz@mail.ru', 2132)
Kolya.set_password()
print(Kolya.check_password(1))
print(Kolya.get_info())
