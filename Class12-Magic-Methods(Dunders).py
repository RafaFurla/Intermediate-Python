class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)


first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)

# ---------------------------------------------
print(' # ' * 40)


class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])


spam = SpecialString("Spam")
hello = SpecialString("Hello World")
print(spam / hello)

# ---------------------------------------------
print(' # ' * 40)


class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(0, len(other.cont)+1):
            results = other.cont[:index] + ">" + self.cont
            results += ">" + other.cont[index:]
            print(results)


spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam > eggs

# ---------------------------------------------
print(' # ' * 40)
import random


class VagueList:

    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self, index):
        return self.cont[index + random.randint(-1, 1)]

    def __len__(self):
        return random.randint(0, len(self.cont)*2)


vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])
