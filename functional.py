from random import randint
class Func:
    def __init__(self, passlen):
        self.passlen = passlen
    def generate(self, passlen):
        y = ""
        for i in range(passlen):
            y += chr(randint(33, 126))
        return y
