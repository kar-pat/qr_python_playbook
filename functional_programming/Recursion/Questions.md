
What is recursion?
Recursion is the practice of defining a function in terms of itself via self-referential expressions

What are the two components of a recursive function?
The two components of a recursive function are the base case and the recursive case. The recursive case needs to be divided into a simpler instance of the problem to be solved. The base case contains the code for handling the simplest version of the recursive function past which the problem cannot be broken into a simpler problem. 

What is tail recursion?
Tail recursion is the method of optimising recursion for memory by computing values as you go. This means that the whole recursion operation doesn't need to happen all at once.

Provide an example of a tail recursive function and a non-tail recursive function.
The example of a tail recursive function can be given using the function that finds a factorial of the number n
def factorial(n):
  if n == 0: return 1
  else: return factorial(n-1) * n

def tail_factorial(n, accumulator=1):
  if n == 0: return accumulator
  else: return tail_factorial(n-1, accumulator * n)
**** But Python does not implement tail-call elimination so what would happen here

Does Python implement tail-call elimination?
Nope

How do you find out the recursion limit?
import sys
sys.getrecursionlimit()

What are the pros and cons of recursion in general? When should you use it?
Recursion is really useful while applying the same solution again and again so should be used in such cases. They are also very useful to reduce the length of the code. However, some drawbacks of recursion are they may cause the c machine to run out of memory and they are very inefficient compared to non -recursive functions.

Compare a recursive function to compute the nth Fibonacci number with an iterative solution.
- What are the differences (efficiency and semantics)?
- What can be done to improve efficiency?
