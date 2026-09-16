# CRT Python Training - Day 11

# Date: 16 September 2026

# FUNCTIONS

# Definition:-

A function is a group/block/collection of statements to perform a specific task.

- By using functions, we can increase the performance of an application.
- We can reduce code repetition in our program.
- A function should contain only repeated code in our program.
- Functions are commonly used in programming languages like C, Java, Python, etc.
- In Python, functions and methods are used.

## Syntax

    def name_of_the_function(parameters):
        statement-1
        statement-2
        statement-3

- `def` is a predefined keyword used to define a function.
- Parameters are optional.
- A function can contain any number of valid statements.
- The statements inside the function form the function block.

## Example

    def addition():
        a, b = map(int, input().split())
        print(a + b)

To execute any function statements, we need to call that function using the function's name.

    addition()

A function can be called any number of times.

## Advantages of Functions

- Code reusability.
- Reduces code repetition.
- Improves readability and maintenance.
- The same function can be used any number of times.
- This concept is common in every programming language.

---

# FUNCTIONS IN C, JAVA AND PYTHON

## C

    void f1(args)
    {
        statements
    }

## Java

    class Abc
    {
        void f1(args)
        {
            statements
        }
    }

## Python

    def f1(args):
        statements

- To define any function in Python, we need to use the predefined keyword `def`.
- Each and every function should contain a valid name.
- The name of the function may contain alphabets, digits and underscore.
- A function name should not start with a digit.
- We can also use uppercase letters as the name of the function.
- It is highly recommended to use lowercase letters as function names because predefined functions are generally in lowercase.

## Examples

    def m1():
        pass

    def m2():
        pass

    def rose():
        pass

    def item2():
        pass

    def pen_cost1():
        pass

    def pen_cost2():
        pass

## Predefined Functions

    print()
    len()
    min()
    max()

## User-Defined Function

    def addition():
        print('Hello')

---

# PARAMETERS

- A function may contain arguments/parameters.
- Arguments may be any type of value such as integer, float, list, etc.
- The values received in a function definition are known as parameters.
- Each and every function should contain business logic in the form of statements.

If a function does not contain statements, we need to use the predefined keyword `pass`.

## Example

    def f1():
        pass

A Python program may contain any number of function definitions.

## Example

    def f1():
        statements

    def f2():
        statements

    def f3():
        statements

If a program contains multiple functions, the names of the functions should be different.

---

# INDENTATION IN FUNCTIONS

While defining any function in Python, we need to follow indentation.

- The statements inside a function should have the same indentation.
- Generally, we use 4 spaces from the starting of the line.
- If a function contains multiple statements, all statements should follow the same indentation.

## Example

    def m1():
        print('Wondrin')

## Multiple Statements

    def m2():
        print('Wondrin')
        print('CSE')
        print('ECE')

If indentation is incorrect, the statement will not belong to the function.

## Example

    def m3():
        print('Wondrin')
        print('CSE')
          print('ECE')

The incorrectly indented statement does not belong to the function block.

---

# FUNCTION CALLING

To execute any function statements, we need to call that function without indentation.

## Example

    def m1():
        print('Pen')
        print('Pencil')

    m1()

To call any function, first we need to define that function.

## Example

    def cse():
        print('Computer Networks')
        print('OOP')
        print('DBMS')
        print('FLAT')
        print('Python')

    cse()

---

# FUNCTIONS WITH ARGUMENTS

- We can pass any type of value from a function call to a function definition.
- To pass values to a function definition from the function call, we need arguments.
- Arguments are separated by commas.
- Arguments may be constant values, variables or expressions.

## Example

    def f1(argument1, argument2, argument3):
        statements

    f1(10, 20, 30)

Here `10`, `20`, and `30` are arguments.

The arguments passed in the function call are received by the parameters in the function definition.

## Example

    def f1(a, b):
        print(a + b)

    f1(10, 20)

---

# POSITIONAL ARGUMENTS

- The number of arguments should be equal to the number of parameters.
- This concept is known as positional arguments.
- In positional arguments, the first argument value is stored in the first parameter.
- The second argument value is stored in the second parameter and so on.

## Example

    def f1(a, b, c):
        print(a, b, c)

    f1(10, 20, 30)

Here:

- `10` is stored in `a`
- `20` is stored in `b`
- `30` is stored in `c`

---

# MULTIPLE CALLS TO A FUNCTION WITH ARGUMENTS

A function can be called multiple times with different argument values.

## Example

    def sum(a, b):
        print(a + b)

    sum(10, 20)
    sum(20, 40)
    sum(30, 50)

We can define a function once and call it multiple times with different values.

---

# FUNCTIONS WITH MULTIPLE STATEMENTS

A function can contain multiple statements.

## Example

    def m1():
        print('Pen')
        print('Pencil')

    def m2():
        print('Black')
        print('Blue')

    def m3():
        print('Red')
        print('Green')

    def m4():
        print('Morning')
        print('Night')

    print('Girl')
    print('Boy')

The statements inside each function should follow proper indentation.

---

# BUSINESS LOGIC IN FUNCTIONS

The statements inside a function may contain business logic such as:

- Initialization
- Reading values
- Checking conditions
- Looping statements
- Calculations
- Returning values

---

# RETURN STATEMENT

- Python functions can return multiple values at a time.
- In C and Java, we generally return only one value at a time.
- Python allows multiple values to be returned.

## Example

    def f1():
        return 10, 20

    a = f1()
    print(a)

The returned values are stored as a tuple.

## Returning Multiple Values

    def f1():
        return 10, 20, 30

    a = f1()
    print(a)

---

# RETURNING DIFFERENT TYPES OF VALUES

Python functions can return different types of values.

## Example

    def f1():
        return 10, '20', 20.5

    a = f1()
    print(a)

A function can return values of different data types.

---

# RETURNING LIST VALUES

A function can also return a list.

## Example

    def m1():
        a, b, c, d = (10, 20, 30, 40)
        return [a, b, c, d]

    a = m1()
    print(a)

---

# RETURNING ELEMENTS AS ARGUMENTS

A function can receive values through arguments and process them.

## Example

    def display(a, b, c):
        return a, b, c

    print(display(10, 20, 30))

---

# NESTED FUNCTIONS

- Python allows us to define a function inside another function.
- The inner function can be called from the outer function.
- This is known as a nested function.

## Example

    def outer_fun():
        print('Hello')

        def inner_fun():
            print('I am in')

        inner_fun()

    outer_fun()

---

# PASSING VALUES AS ARGUMENTS

We can pass values as arguments in the function call.

## Example

    def inner_fun(a, b):
        return a + b

    print(inner_fun(10, 20))

The values `10` and `20` are passed as arguments.

---

# FUNCTION WITH RETURN VALUE

A function can return a value using the `return` statement.

## Example

    def outer_fun():
        def inner_fun():
            return 10 + 20

        return inner_fun()

    print(outer_fun())

---

# FUNCTION WITH DIFFERENT INNER FUNCTIONS

A function can contain different inner functions.

## Example

    def outer():
        def inner1():
            print('I am in')

        def inner2():
            print('I am in')

        def inner3():
            print('I am in')

        inner1()
        inner2()
        inner3()

    outer()

---

# FUNCTION CALLING

To execute the statements of a function, we need to call the function.

## Example

    def m1():
        print('Python')

    m1()

- First define the function.
- Then call the function using its name.
- A function can be called any number of times.
- Functions help in code reusability and reduce repetition.
