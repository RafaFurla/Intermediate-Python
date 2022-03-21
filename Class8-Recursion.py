def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(5))
# ---------------------------------------
print(' - ' * 40)


def is_even(x):
    print(f'Par {x}')
    if x == 0:
        return True  # this adds a "true" to the result when the number pass by here at the end of jorney.
    else:
        return is_odd(x - 1)


def is_odd(x):
    print(f'Impar {x}')
    return not is_even(x)  # this adds a "not" to the result every time the number pass by here.


print(is_odd(3))

