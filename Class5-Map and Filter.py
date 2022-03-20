# Map
print('Map')


def add_five(x):
    return x + 5


nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)
# Map with Lambda:
print('Map with Lambda')
nums = [11, 22, 33]
a = list(map(lambda x: x*2, nums))
print(a)
# ---------------------------------------------------
# Filter
print('Filter')
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x % 2 == 0, nums))
print(res)
