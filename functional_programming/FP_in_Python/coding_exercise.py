"""
Choose some functions from more-itertools (https://more-itertools.readthedocs.io/en/stable/index.html)
and try to implement them yourself.

Suggestions:
- `chunked`
- `spy`
- `windowed`

You can compare your attempts with the actual implementation afterwards.
"""
import itertools
import operator
from more_itertools import chunked

a = [1, 2, 3, 4 , 5, 6]
b=[1, 3,5,7,9]
c = operator.add(a, b)
print(c)

d = chunked(a,2)
print(list(d))
