def function(named_arg, *args):
    print(named_arg)
    print(args)


function('Name', 1, 2, 3, 4)
# -----------------------------------------------
print(' - ' * 40)


def my_func(x, y, *args, **kwargs):
    print(x)
    print(y)
    print(args)
    print(kwargs)


my_func(10, 11, 1, 2, 3, a=7, b=8)
