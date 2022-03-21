class Wolf:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Grr...")


class Dog(Wolf):  # This method is exactly equal to the method bark inside Wolf Class. What will happens is that the
                  # Dog bark method will override the Wolf bark Method.
    def bark(self):
        print("Woof")


husky = Dog("Max", "grey")
husky.bark()
