"""
Convert these non-functional code examples into functional examples,
using `map`, `filter` and `reduce`.
"""

from functools import reduce


# Convert this into a one-liner in functional style, using `map`:
squares = []
for i in range(10):
    squares.append(i**2)
print(squares)

#Using map
def square_method(x):
    return x**2
squares1 = list(map(square_method, (i for i in range(10))))
print (squares1)

# Now only include odd `i`, using `filter`:
odd_squares = []
for i in range(10):
    if i % 2 != 0:
        odd_squares.append(i**2)
print(odd_squares)

#Using filter
def filtered_numbers(x):
    return True if x % 2 != 0 else False

odd_squares1 = list(filter(filtered_numbers, (square_method(x) for x in range(10))))
print (odd_squares1)


# Now get the sum of the resulting list, using `reduce` (do not use the built-in `sum`):
odd_squares_sum = 0
for i in range(10):
    if i % 2 != 0:
        odd_squares_sum += i**2
print(odd_squares_sum)

#using reduce
odd_squares_sum = reduce(lambda x, y: x+y, odd_squares1)
print (odd_squares_sum)