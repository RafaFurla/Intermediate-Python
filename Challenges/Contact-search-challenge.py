contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]
k = int(-1)
name = str(input('input the name of the contact: ')).strip()
for c in range(0, len(contacts)):
    if contacts[c][0] == name:
        k = c
if k != -1:
    print(f'{contacts[k][0]} is {contacts[k][1]}')
else:
    print('Not found')
