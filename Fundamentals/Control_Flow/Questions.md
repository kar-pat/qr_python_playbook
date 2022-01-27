
What does `pass` do?
A pass statement does nothing, it is useful in development code or when the functionality is to be added in the future. wherein you write a function or any code such as loop and use pass to implement it sometime in the future.

What is a ternary statement?
A ternary statement is a if-else one liner, they evaluate the one-line statement on the basis on the condition mentioned being true
e.g. Print "Kartik" if x=1 else "not Kartik" 

When should you use a for loop or a while loop and why would you pick one over the other?
A for loop is used when looping between a range with a definite ending, whereas a while loop can be executed indefinitely until the required condition turns true

How does the `else` clause on a for loop work?
The else clause can be used to implement code that completes only after the loop completes normally, e.g. if there is a break clause in the for loop, then the else clause code will only be run if the for loop doesn't break.

How can you skip an iteration in a loop?
an iteration in a loop can be skipped using a continue statement.

How can you cancel a loop prematurely?
using a break statement.

Why are functions useful?
Functions are useful because they help in writing clean code such that each function executes one particular action therefore improving readability and making it easier to debug. Furthermore, they facilitate a quicker way to implement the same bit of code multiple times.

What is a side effect?
a function is said to have a side effect if the global variable gets updated within a function.

How does Python handle arguments passed to functions? e.g. Is the argument value copied to a new variable? each argument passed is assigned to the variable mentioned in the argument section whil edefining the function. 


What is the difference between global and local variables in functions?
Global variables are variables that are set outside the function whereas local variables are set within the function. 

How do you set defaults for function arguments?
Default arguments can be set by assigning default values to arguments while defining the function. 

How would you set an argument default to an empty list?

What are positional and keyword arguments?
Positional arguments are arguments that are interpreted and assigned to their input position whereas keyword arguments need to be specified along with the keyword to be used in a function. 

How do `*args` and `**kwargs` work?
they refer to tuple and dictionary unpacking respectively and can be used to supply a funciton with multiple arguments.

What are function annotations?
Function annotations are function metadata that is generally for the whole fucntion put using ''' and using a : for variables etc. this function metadata isn't executed but makes code documentation much easier.

How do you return multiple values, and how can you assign those returned values?
you return multiple values by separating the multiple values using a comma, they can also be assigned using a comma or you can use keyword only fcntion by making a dummy *somearg.