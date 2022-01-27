"""
Rewrite the following using comprehensions.
"""

cubes = []
for x in range(30):
    if x % 3 == 0:
        cubes.append(x**3)


times_table = []
for x in range(10):
    row = []
    for y in range(10):
        row.append(x * y)
    times_table.append(row)


hours = set()
for h in range(24 * 7):
    hours.add(h % 24)


exp_table = {}
for x in range(10):
    for y in range(10):
        exp_table[(x, y)] = x ** y


chars = {}
for char in "abcde":
    chars[char] = []
    for num in range(5):
        chars[char].append(f"{char}{num}")
