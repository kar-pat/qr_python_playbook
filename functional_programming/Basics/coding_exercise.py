"""
Convert these non-functional code examples into functional examples,
using `map`, `filter` and `reduce`.
"""

# Convert this into a one-liner in functional style, using `map`:
squares = []
for i in range(10):
    squares.append(i**2)
print(squares)


# Now only include odd `i`, using `filter`:
odd_squares = []
for i in range(10):
    if i % 2 != 0:
        odd_squares.append(i**2)
print(odd_squares)


# Now get the sum of the resulting list, using `reduce` (do not use the built-in `sum`):
odd_squares_sum = 0
for i in range(10):
    if i % 2 != 0:
        odd_squares_sum += i**2
print(odd_squares_sum)
