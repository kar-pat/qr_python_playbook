
What is lambda calculus?

What are the benefits of FP?
The benefits of functional programming are 
modularity
ease of debugging 
provability

What are higher order functions?
high order functions are functions that operate on other functions.

What is currying?
currying refers to simplyfying functions that take multiple arguments into sequential signle argument fucntions. 
What is lazy evaluation, and what are the pros/cons?
lazy evaluation delays the evaluation of an expression until the value of that expression is needed. it has its pro is helping optimise code once written as well as to provide useful abstractions. However, the drawbacks exist where the code requires strict evaluation, such as if the name of a person needs to be input right now before the code can move forward

What is the continuation-passing style?
continuations allow returning the evaluated value of a function to another function rather than the caller. e.g. int i = add(5, 10);
int j = square(i);

int j = add(5, 10, square);


What is a closure?
Closure helps keep the variables of a function even after the function has exited. Useful way to understand it from Stack Overflow:

outer = function() {
  var a = 1;
  var inner = function() {
    console.log(a);
  }
  return inner; // this returns a function
}

var fnc = outer(); // execute outer to get inner 
fnc();

Here I have defined a function within a function. The inner function gains access to all the outer function's local variables, including a. The variable a is in scope for the inner function.

Normally when a function exits, all its local variables are blown away. However, if we return the inner function and assign it to a variable fnc so that it persists after outer has exited, all of the variables that were in scope when inner was defined also persist. The variable a has been closed over -- it is within a closure.

Note that the variable a is totally private to fnc. This is a way of creating private variables in a functional programming language such as JavaScript.

As you might be able to guess, when I call fnc() it prints the value of a, which is "1".

In a language without closure, the variable a would have been garbage collected and thrown away when the function outer exited. Calling fnc would have thrown an error because a no longer exists.

In JavaScript, the variable a persists because the variable scope is created when the function is first declared and persists for as long as the function continues to exist.

a belongs to the scope of outer. The scope of inner has a parent pointer to the scope of outer. fnc is a variable which points to inner. a persists as long as fnc persists. a is within the closure.