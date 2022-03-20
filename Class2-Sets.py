num_set = {1, 2, 2, 2, 2, 3, 4, 5}
print(3 in num_set)
print(len(num_set))
# ---------------------------------------
print('-' * 40)
nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(1)
print(nums)
# ---------------------------------------
print('-' * 40)
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}
print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)
# ---------------------------------------
print('-' * 40)
cubes = [i**3 for i in range(5)]
print(cubes)
# ---------------------------------------
print('-' * 40)
evens = [i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)
# ---------------------------------------
print('-' * 40)
text = input().strip().lower()
dict = {}
for c in range(0, len(text)):
    dict[text[c]] = text.count(text[c])
print(dict)
