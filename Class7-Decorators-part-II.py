def decor(func):
    def wrap():
        print('=' * 20)
        func()
        print('=' * 20)
    return wrap


@decor  # the @decor will apply the function decor to our print_text function transforming it.
def print_text():
    print(f'{"Hello World!":^20}')


print_text()
