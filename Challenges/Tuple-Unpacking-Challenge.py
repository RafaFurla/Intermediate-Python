def calc(x):
    tup = (4 * x, x**2)
    return tup


side = int(input())
p, a = calc(side)

print("Perimeter: " + str(p))
print("Area: " + str(a))
