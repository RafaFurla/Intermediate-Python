def my_func(f, arg):
    return f(arg)


print(my_func(lambda x: 2*x*x, 5))
# -----------------------------------------
print('-+-' * 20)
print('Named function:')


def polynomial(x):
    return x**2 + 5*x + 4


print(polynomial(-4))
# -----------------------------------------
print('-+-' * 20)
print('Lambda function:')
print((lambda x: x**2 + 5*x + 4)(-4))
