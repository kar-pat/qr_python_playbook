"""
Write a decorator that will print a message before and after the function it wraps.

>>> @surround
... def my_func():
...    print("my func is running")
... my_func()
before
my func is running
after

Now modify your decorator so that the messages can be configured.

>>> @surround(before="before the func", after="after the func")
... def my_func():
...     print("my func is running")
... my_func()
before the func
my func is running
after the func


Write a decorator that will print the args and kwargs the wrapped function was
called with.

>>> @log_args_and_kwargs
... def my_func(*args, **kwargs):
...     pass
... my_func(0, 1, a=2, b=3)
args=(0, 1)
kwargs={'a': 2, 'b': 3}


Write a decorator that writes the return value to a file.

>>> @write_to_file("filename.txt")
... def my_func():
...     return "Hello World!"
... print(my_func())
Hello World!

filename.txt:
Hello World!
"""
