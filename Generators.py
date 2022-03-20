print('Generators')
def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1


for i in countdown():
    print(i)
# --------------------------------------------
"""print('Infinite Generator')


def infinite_sevens():
    while True:
        yield 7


for i in infinite_sevens():
    print(i)"""
# --------------------------------------------
print('Converting generators into lists')


def numbers(x):
    for i in range(0, x):
        if i % 2 == 0:
            yield i


print(list(numbers(11)))
