
What is a namespace and what are some examples?
A namespace is a collection of currently defined symbolic names along with information about the object that each name references. You can think of a namespace as a dictionary in which the keys are the object names and the values are the objects themselves. 

In Python, is a class an object?
Yes, classes are objects. 

What things are objects in Python?###
Modules are objects, class definitions and functions are objects, and of course, objects created from classes are objects too.

What is an attribute?
Attributes are characteristics unique to a class or an instance, which help us identify the class or the instance. The Class attributes are defined directly after the class name and the instance attributes are defined as part of the `__init__` method. Then when an instance is created the values are assigned to the instance attributes.

What is `__init__` for?
`__init__` sets the initial state of the object by assigning the attribute values when the object is assigned under a particular class, thereby initialising each new instance of a class. The attributes assigned by init are instance attributes

What are `__str__` and `__repr__`?
Like `__init__`, `__str__` and `__repr__` are dunder methods. String is useful when someone calls the object using str(object) or print(object) and repr is useful when someone simply types the name of the object. `__repr__` is particularly useful for debugging by developers.
What is the difference between instance and class attributes?
The class attributes are defined directlty after the class name and are same for all instances of that class, whereas the instance attributes are defined in the `__init__` method and values are assigned when creating instances. The instance attributes are unique to every instance and help provide a unique identity to the instances.

What is `self`?
`self` refers to the class itself, when the class is initialised, or any method is defined it needs to refer to the class to be a class method and this is what self does

How does an instance method automatically set the `self` argument? What is an equivalent way to call it using the class?

How do you create an instance of a class?
To create an instance of the class we define the instance with the class names and assign instance attributes in brackets.

How does Python do inheritance?

How does multiple inheritance work?

What is a mixin?

How do you override a method?
To override a method of the parent class you define a method with the similar name on the child class

What is `super()` for?

How do you check if an object is an instance of a certain class?
using the `isinstance()` method

How do you check if an object is an instance of a certain class or any of its parent classes?

What are the conventions for private variables?

Are private variables accessible from outside the class?

What are the differences between instance methods, class methods and static methods?

What is method resolution order (MRO) and how does it work?

When would you choose to use inheritance or composition?
