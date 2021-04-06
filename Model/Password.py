from random import choice, randint


class Password:
    def __init__(self, length, struct):
        self.password = ''
        self.length = length
        self.data = dict()
        self.struct = ['alphabet', ]
        self.data['alphabet'] = 'abcdefghijklmnopqrstuvwxyz'
        if 0 in struct:
            self.data['numbers'] = '0123456789'
            self.struct.append('numbers')
        if 1 in struct:
            self.data['alphabet_title'] = self.data['alphabet'].upper()
            self.struct.append('alphabet_title')
        if 2 in struct:
            self.data['signs'] = r'!@#$%^&*()><,.}[]\{'
            self.struct.append('signs')

    def generate_password(self):
        for sign in range(self.length):
            self.password += choice(self.data[choice(self.struct)])





