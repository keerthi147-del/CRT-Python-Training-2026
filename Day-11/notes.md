# CRT Python Training - Day 10

## Topic: Functions

### 1. Definition of Function

A function is a group/block or collection of statements to perform a specific task.

### Advantages of Functions

- By using functions, we can increase the performance of an application.
- We can reduce code repetition in our program.
- A function should contain the repeated code in our program.
- Code reusability is one of the main advantages of functions.
- We can write the code once and use it any number of times.
- This concept is common in every programming language.

---

## 2. Syntax of Function

To define a function in Python, we use the predefined keyword `def`.

### Syntax

    def function_name(parameters):
        statement-1
        statement-2
        statement-n

- `def` is the predefined keyword used to define a function.
- `function_name` is the name of the function.
- `parameters` are optional.
- The statements inside the function form the function body.
- The function body should follow proper indentation.

### Example

    def addition():
        a, b = map(int, input().split())
        print(a + b)

---

## 3. Function Name

To define a function in Python, we need to use a valid name for the function.

- The name of the function may be any alphabet or any word.
- Function names can also contain digits, but they should not start with a digit.
- We can use uppercase letters as function names.
- However, it is highly recommended to use lowercase letters for function names because predefined functions are generally written in lowercase.

### Examples

    def nil():
        pass

    def me():
        pass

    def cost():
        pass

    def item2():
        pass

    def pen_cost():
        pass

    def pen_cost1():
        pass

---

## 4. Function Statements

Each and every function should contain a valid statement.

A function may contain business logic such as:

- Initialization
- Reading values
- Checking values
- Looping statements
- Other required program statements

If a function does not contain any statement, we need to use the predefined keyword `pass`.

### Example

    def f1():
        pass

---

## 5. Multiple Function Definitions

A Python program may contain any number of function definitions.

Example:

    def f1():
        pass

    def f2():
        pass

    def f3():
        pass

If a program contains multiple functions, the names of the functions should be different.

---

## 6. Indentation in Functions

While defining a function in Python, we need to follow indentation.

- The function statements should be indented from the starting of the function.
- We normally use 4 empty spaces for indentation.
- If a function contains multiple statements, all statements belonging to that function should have the same indentation.

### Example

    def m2():
        print("wondini")
        print("cse")
        print("e")

The statements inside the function belong to `m2()` because they have the same indentation.

---

## 7. Calling a Function

To execute any function statement, we need to call that function using its function name.

### Example

    def cse():
        print("CSE")

    cse()

Here:

- `def cse():` is the function definition.
- `cse()` is the function call.

To call any function, we first need to define that function.

---

## 8. Calling a Function Multiple Times

We can call a function any number of times.

### Example

    def fun():
        print("Python")

    fun()
    fun()
    fun()

The same function can be reused multiple times without writing the same code again.

---

## 9. Functions with Multiple Statements

A function can contain multiple statements.

### Example

    def m1():
        print("pen")
        print("pencil")

    def m2():
        print("Black")
        print("Blue")

    def m3():
        print("Red")
        print("Green")

    def m4():
        print("Morning")
        print("Night")

    print("Girl")
    print("Boy")

The statements inside each function should follow proper indentation.

---

## 10. Function Example

We can define a function to print our department/subject names and then call the function.

### Example

    def sub():
        print("Computer Networks")
        print("OOP")
        print("OS")
        print("FLAT")
        print("DBMS")

    sub()

---

## 11. Functions with Arguments

We can pass any type of value from a function call to a function definition.

To pass values from the function call to the function definition, we use arguments and parameters.

- Arguments are the values passed during the function call.
- Parameters are used in the function definition to receive those values.
- Arguments may be values such as integers, floats, lists, etc.
- Arguments are separated by commas.

### Syntax

    function_name(argument1, argument2, ..., argumentN)

### Example

    def f2(a, b):
        print(a + b)

    f2(10, 20)

Here:

- `a` and `b` are parameters.
- `10` and `20` are arguments.

---

## 12. Types of Values Passed as Arguments

Arguments may be:

- Constant values
- Variables
- Expressions

### Examples

    f1(10, 20, 30)

    a = 10
    b = 20
    f1(a, b)

    a = 8
    b = 11
    f1(a + 10, b + 20)

---

## 13. Positional Arguments

The number of arguments should be equal to the number of parameters.

This concept is known as positional arguments.

In positional arguments:

- The first argument value is stored in the first parameter.
- The second argument value is stored in the second parameter.
- The third argument value is stored in the third parameter.
- This continues according to their positions.

### Example

    def f1(a, b, c):
        print(a, b, c)

    f1(10, 20, 30)

Here:

- `10` is assigned to `a`.
- `20` is assigned to `b`.
- `30` is assigned to `c`.

---

## 14. Multiple Ways to Call a Function with Arguments

A function with arguments can be called in different ways.

### Case 1: Using variables

    a = 10
    b = 20
    print(a + b)

### Case 2: Passing values directly

    print(10 + 20)

### Case 3: Defining a function and calling it

    def sum(a, b):
        print(a + b)

    sum(10, 20)

### Case 4: Calling the same function multiple times

    def sum(a, b):
        print(a + b)

    sum(10, 20)
    sum(20, 40)

The same function can be reused with different argument values.

---

## 15. Important Points About Functions

- A function is used to perform a specific task.
- Functions help reduce code repetition.
- Functions provide code reusability.
- A function is defined using the `def` keyword.
- A function must have a valid function name.
- Parameters are optional.
- Arguments are passed during a function call.
- Parameters receive the argument values.
- The number of positional arguments should be equal to the number of parameters.
- Function statements must follow proper indentation.
- If a function does not contain statements, the `pass` keyword can be used.
- A Python program can contain multiple function definitions.
- We can call a function any number of times.
