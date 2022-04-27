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
import functools


#1 Decorator that does stuff before and after function
def surround(func):
    @functools.wraps(func)
    def wrapper():
        print("the function is about to be run")
        func()
        print("the function run is completed")
    return wrapper

@surround
def my_func():
    print("my function is running")

#2 Decorator that takes arguments

def surround1(_func=None, before="before the func", after="after the func"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper():
            print("the function is about to be run")
            func()
            print("the function run is completed")
        return wrapper
    return decorator(_func) if _func else decorator

@surround1(before='The function is about to be run', after='The function run is completed')
def my_func1():
    print('Kartik')    

#Decorator that prints args and kwargs that the wrapped funtion is called with
def log_args_and_kwargs(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'args={args}', f'kwargs={kwargs}')
        return func(*args, **kwargs)
    return wrapper

@log_args_and_kwargs
def my_func2(*args, **kwargs):
    pass

def write_to_file(filename):
    def file_write_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with open(filename, 'w') as file:
                file.write(func(*args, **kwargs))
        return wrapper
    return file_write_decorator

@write_to_file('Kartik.csv')
def my_func3():
    return 'Hello World!'



my_func()
my_func1()
my_func2(0, 1, a=2, b=3)
my_func3()