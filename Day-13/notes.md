# CRT Python Training - Day 13

## Topic: Advanced Functions & Function Arguments

### Date: 17 September 2026


## 1. Nested Function Calling

A function can be defined inside another function.

The inner function can be called only from inside the outer function.

Example:

    def outer_fun():
        print('Hello')

        def inner_fun():
            print('I am inner function')

        inner_fun()

    outer_fun()

---

## 2. Returning Multiple Values

Python allows a function to return multiple values at a time.

We can return multiple values by separating them with commas.

Example:

    def inner_fun():
        return 10, 20

    a = inner_fun()
    print(a)

Output:

    (10, 20)

The returned values are stored as a tuple.

---

## 3. Returning Different Types of Values

A function can return different types of values.

Example:

    def inner_fun():
        return 10, 20, 'hello'

    a, b, c = inner_fun()

    print(a)
    print(b)
    print(c)

---

## 4. Passing Values as Arguments

Values can be passed to a function through arguments.

Example:

    def outer_fun():
        def inner_fun(a):
            print(a)

        inner_fun(10)

    outer_fun()

---

## 5. Function with Multiple Arguments

A function can accept multiple arguments.

Example:

    def outer_fun():
        def inner_fun(a, b, c):
            print(a, b, c)

        inner_fun(10, 20, 30)

    outer_fun()

---

# Types of Function Arguments

There are different ways of passing arguments to a function:

1. Positional Arguments
2. Keyword Arguments
3. Default Arguments
4. Variable-Length Arguments
5. Keyword-Only Arguments
6. Positional-Only Arguments

---

## 6. Positional Arguments

In positional arguments, values are passed according to their position.

Example:

    def details(name, age):
        print(name)
        print(age)

    details('Keerthi', 20)

Here, 'Keerthi' is passed to name and 20 is passed to age.

---

## 7. Keyword Arguments

In keyword arguments, values are passed using parameter names.

Example:

    def details(name, age):
        print(name)
        print(age)

    details(age=20, name='Keerthi')

Here, the order of arguments does not matter because the parameter names are specified.

---

## 8. Default Arguments

Default arguments are parameters that have default values.

If no value is passed, the default value is used.

Example:

    def details(name='Keerthi', age=20):
        print(name)
        print(age)

    details()

We can also change the default values by passing new values.

Example:

    details('Deekshitha', 20)

---

## 9. Variable-Length Positional Arguments - *args

Sometimes we do not know how many positional arguments will be passed.

In such cases, we can use *args.

*args accepts any number of positional arguments.

Example:

    def display(*details):
        print(details)

    display('Keerthi', 20)

The values passed using *args are stored in a tuple.

Examples:

    display(10, 20)
    display(10, 20, 30, 40)
    display(10, 20, 30)

Output:

    (10, 20)
    (10, 20, 30, 40)
    (10, 20, 30)

---

## 10. Keyword-Only Parameters - *

A * can be used to make the parameters after it keyword-only.

The keyword-only parameters must be passed using their parameter names.

Example:

    def details(name, *, salary, exp):
        print(name, salary, exp)

    details('Keerthi', salary=25000, exp=10)

Here, salary and exp are keyword-only parameters.

---

## 11. Positional-Only Parameters - /

A / is used to make parameters before it positional-only.

The positional-only parameters must be passed by position.

Example:

    def details(name, age, /):
        print(name, age)

    details('Keerthi', 20)

The following type of calling is not allowed for positional-only parameters:

    details(name='Keerthi', age=20)

Because name and age are positional-only parameters.

---

## 12. Variable-Length Keyword Arguments - **kwargs

Sometimes we do not know how many keyword arguments will be passed.

In such cases, we can use **kwargs.

**kwargs accepts any number of keyword arguments.

The values are stored in the form of a dictionary.

Example:

    def details(**data):
        print(data)

    details(name='Keerthi', age=20, course='Python')

Output:

    {'name': 'Keerthi', 'age': 20, 'course': 'Python'}

---

## 13. Using *args and **kwargs

A function can accept both variable-length positional and keyword arguments.

Example:

    def details(*args, **kwargs):
        print(args)
        print(kwargs)

    details(10, 20, 30, name='Keerthi', course='Python')

Here:

- *args stores positional arguments as a tuple.
- **kwargs stores keyword arguments as a dictionary.

---

## Key Points

- A function can contain another function.
- The inner function can be called from the outer function.
- A function can return multiple values.
- Multiple returned values are generally stored in a tuple.
- Arguments can be passed positionally or using keywords.
- Default arguments provide default values to parameters.
- *args accepts any number of positional arguments.
- **kwargs accepts any number of keyword arguments.
- * is used for keyword-only parameters.
- / is used for positional-only parameters.
- Keyword-only arguments must be passed using parameter names.
- Positional-only arguments must be passed according to their position.
