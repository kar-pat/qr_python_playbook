"""
Rewrite the following using comprehensions.
"""

cubes = []
for x in range(30):
    if x % 3 == 0:
        cubes.append(x**3)

cubes1 = [i**3 for i in range(1,30)]

times_table = []
for x in range(10):
    row = []
    for y in range(10):
        row.append(x * y)
    times_table.append(row)

timetable1 = [x*y for x in range(10) for y in range(10)]

hours = set()
for h in range(24 * 7):
    hours.add(h % 24)

hours1 = set(h%24 for h in range(24 * 7))

exp_table = {}
for x in range(10):
    for y in range(10):
        exp_table[(x, y)] = x ** y

exp_table1 = {(x,y):x**y for x in range(10) for y in range(10)}


chars = {}
for char in "abcde":
    chars[char] = []
    for num in range(5):
        chars[char].append(f"{char}{num}")

chars1 = {char:[(f"{char}{num}") for num in range(5)] for char in "abcde"}
print(chars1)
