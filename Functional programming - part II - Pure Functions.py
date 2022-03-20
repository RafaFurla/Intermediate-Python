# PURE FUNCTIONS
def pure_function(x, y):
    temp = x + 2*y
    return temp / (2*x + y)


print(pure_function(2, 3))
print(pure_function(2, 3))
print('-' * 40)

# IMPURE FUNCTIONS
some_list = []


def impure(arg):
    some_list.append(arg)


impure(2)
print(some_list)
impure(2)
print(some_list)
