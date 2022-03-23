class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs


class SpecialCats:
    pass  # we use this command "pass" when we create a class but we don't know yet how the functions
    # will be. Then we pass right now to create the functionalities latter.


felix = Cat("ginger", 4)
rover = Cat("dog_colored", 4)
stumpy = Cat("brown", 3)
bibi = SpecialCats()
print(bibi)  # Bibi is in the class "Special Cats" and we don't finish this class yet. Then if we print
# Bibi we will obtain just the address of the allocated memory for Bibi that is: 0x0000014AB34A2B90.
