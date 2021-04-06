from Model.Password import Password


class Controller:
    def __init__(self):
        self.password = ''

    def create_pas(self, length, struct):
        self.password = Password(length, struct)
        self.password.generate_password()

        return self.password.password