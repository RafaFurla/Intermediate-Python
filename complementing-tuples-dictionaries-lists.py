pairs = {
    1: "apple",
    "orange": [2, 3, 4],
    True: False,
    12: "True"
}
print(pairs.get("orange", "Blue"))
print(pairs.get(7, 42))
print(pairs.get(12345, "not found"))
# ---------------------------------------------
print('-' * 40)
data = {
    'Singapore': 1,
    'Ireland': 6,
    'United Kingdom': 7,
    'Germany': 27,
    'Armenia': 34,
    'United States': 17,
    'Canada': 9,
    'Italy': 74
}
n = str(input('Input a country: '))
print(f'{data.get(n, "Country Not found")} in economic liberty ranking!')
# ---------------------------------------------
print('-' * 40)
numbers = (1, 2, 3)
a, b, c = numbers
print('''numbers = (1, 2, 3)
a, b, c = numbers''')
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')
# ---------------------------------------------
print('-' * 40)
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('''a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]''')
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')
print(f'd = {d}')
# ---------------------------------------------
print('-' * 40)
a, b, c, d, *e, f, g = range(20)
print(f'{a}, {b}, {c}, {d}, {e}, {f}, {g}')