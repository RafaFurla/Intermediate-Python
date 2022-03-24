class NUMBER:
    def __init__(self, cont):
        self.cont = cont

    def __add__(self, other):
        soma = self.cont + other.cont
        return soma

    def __radd__(self, other):
        rsoma = self.cont + other
        return rsoma


x = int(12)
y = NUMBER(8)
print(x + y)
