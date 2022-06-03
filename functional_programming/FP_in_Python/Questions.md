
What are iterators?
Iterators are python objects that can be iterated upon i.e. we can traverse through each of their values one by one. They should be able to iterate thye __iter__ and __next__() methods to be an iterator object. Examples of iterators are lists, tuples, string etc.
What are generators (including generator expressions)?
Generators are a special type of function that don't throw away the local variables after exiting the function. They contain the yield keyword insteead of return. Yield is different from return in the sense that the function isnt exited after yield and the state of the fucntion is remembered that way the next iteration can be called using next() method
When is it preferable to use generators?
It is preferable to use generators when the size of the iterable is extremely large. This is becasue generators help optimise memory as we can create them wihtou holding the entire iterable object in memory.
What does `zip` do?
`zip` returns an iterator of tuples wherein the i^th tuple contains the ith element from each of the iterable objects supplied to zip. 

What are `functools` and `itertools` modules?
Both `functools` and `itertools` modules contain higher order function that can be applied to callable objects

What does `itertools.chain` do?
`itertools.chain` returns elements from two or more iterable objects sequentially wherein it moves to the elements of the subsequent iterable object after it has exhaisted all the elements of the first iterable object.

Why is the `operator` module useful for functional programming?
??  Helps do python operations on callable objects??
What is `functools.partial`?
`functools.partial` is a function of the functools module that freezes a portion of the functions arguments resulting in a new object with a simplified signature.