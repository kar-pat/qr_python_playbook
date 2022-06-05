"""
Write a recursive function to reverse a sequence.

>>> reverse('abcdef')
'fedcba'
>>> reverse([0, 1, 2, 3, 4])
[4, 3, 2, 1, 0]
>>> reverse(('x', 'y', 'z', 1, 2))
(2, 1, 'z', 'y', 'x')

Is your function tail recursive?
Yes, while python  doesn't have a tail call optimisation, lru_cache helps us avoid separately computing every elemetn of the list.  

If it isn't, how can you change it so that it is?

Given what you have just learned about recursion in Python,
which solution do you prefer and why?
Tail recursive or the one that caches the result in our case as itiscomputationally cheaper. 
"""


from functools import lru_cache


@lru_cache(maxsize=None)
def reverse(seq):
    if len(seq) == 1:
        return seq
    else:
        return seq[-1] + reverse(seq[:-1])

print(reverse("abcdef"))
print(reverse([0, 1, 2, 3, 4]))
print(reverse(('x', 'y', 'z', 1, 2)))