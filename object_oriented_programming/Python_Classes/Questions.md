
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
When a class is declared as an inheritance, the new class inherits all the  attributes of the parent class. To prevent duplicating code, we can use super() to implement all methods of the parent class in one line. The inherited methods can be overwritten by rewriting the method with the same name in the child class.

How does multiple inheritance work?
In multiple inheritance the child class inherits all the attributes of multiple parent classes, when the parent classes are declared as arguments in the constructor. 

What is a mixin?
Mixin is a basic class that has a   behavior to be inherited by a class, to do this it is spevified in the constructor of the child class. 

How do you override a method?
To override a method of the parent class you define a method with the similar name on the child class

What is `super()` for?
`super()` is a method used to inherit the methods of the parent class to the subclasses while avoiding code repititions.

How do you check if an object is an instance of a certain class?
using the `isinstance()` method

How do you check if an object is an instance of a certain class or any of its parent classes?

What are the conventions for private variables?

Are private variables accessible from outside the class?
no

What are the differences between instance methods, class methods and static methods?


What is method resolution order (MRO) and how does it work?
method resolution order is the order that decides which parent classes to search for methods in to be implemented. It follows the order in which the methods are declared in the class constructor.

When would you choose to use inheritance or composition?
1. Use inheritance over composition in Python to model a clear is a relationship. First, justify the relationship between the derived class and its base. Then, reverse the relationship and try to justify it. If you can justify the relationship in both directions, then you should not use inheritance between them.
2. Use inheritance over composition in Python to leverage both the interface and implementation of the base class.
3. Use inheritance over composition in Python to provide mixin features to several unrelated classes when there is only one implementation of that feature.
4. Use composition over inheritance in Python to model a has a relationship that leverages the implementation of the component class.
5. Use composition over inheritance in Python to create components that can be reused by multiple classes in your Python applications.
6. Use composition over inheritance in Python to implement groups of behaviors and policies that can be applied interchangeably to other classes to customize their behavior.
7.     Use composition over inheritance in Python to enable run-time behavior changes without affecting existing classes.