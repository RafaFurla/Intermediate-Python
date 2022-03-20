def decor(func):
    def wrap():
        print('=' * 20)
        func()
        print('=' * 20)
    return wrap


def print_text():
    print(f'{"Hello World!":^20}')


decorated = decor(print_text)
decorated()
# ------------------------------------------
print()
print(' # ' * 20)
print()
print_text = decor(print_text)
print_text()
# ------------------------------------------
print()
print(' # ' * 20)
print()
decorated = decor(print_text)
decorated()
# ------------------------------------------
