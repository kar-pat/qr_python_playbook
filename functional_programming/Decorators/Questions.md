
What is a decorator?
a decorator is a function that takes another function and extends the behaviour of the previous function to a the new function.

What is the decorator syntax equivalent to?
The decorator syntax is equivalent to calling a function inside the pther function to extend the behaviour of the function being called.

What does `functools.wraps` do?
functools.wraps helps preserve the information about the original function rather than get the identity of the inner function of the decorator.


Give some examples of appropriate uses of decorators
Decorators are useful in debugging code, slowing down functions, registering plugins, caching return values


How can decorators be used as a lightweight way to register plugins?
Decorators can be used to register plug-ins by writing a decorator that has an inner function writing the name of the plug in to a dictionary.

How do you combine multiple decorators on a single function?
Multiple decorators can be combined by @ them before the start of the function.

How can you make a decorator take arguments?
A decorator can be made to take arguments using an inner function that takes arguments using *args **kwargs and returning that fucntion
