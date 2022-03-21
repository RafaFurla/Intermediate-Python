class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print('Woof!')


fido = Dog("Fido", "brown")
print(fido.name)
print(fido.color)
fido.bark()
