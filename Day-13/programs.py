
## 🐍 Day-13/programs.py


# CRT Python Training - Day 13
# Date: 17 September 2026
# Topic: Advanced Functions & Function Arguments


# 1. Nested Function Calling

def outer_fun():
    print('Hello')

    def inner_fun():
        print('I am inner function')

    inner_fun()


outer_fun()


# 2. Returning Multiple Values

def inner_fun():
    return 10, 20


a = inner_fun()
print(a)


# 3. Returning Different Types of Values

def inner_fun():
    return 10, 20, 'hello'


a, b, c = inner_fun()

print(a)
print(b)
print(c)


# 4. Passing Values as Arguments

def outer_fun():
    def inner_fun(a):
        print(a)

    inner_fun(10)


outer_fun()


# 5. Function with Multiple Arguments

def outer_fun():
    def inner_fun(a, b, c):
        print(a, b, c)

    inner_fun(10, 20, 30)


outer_fun()


# 6. Positional Arguments

def details(name, age):
    print(name)
    print(age)


details('Keerthi', 20)


# 7. Keyword Arguments

def details(name, age):
    print(name)
    print(age)


details(age=20, name='Keerthi')


# 8. Default Arguments

def details(name='Keerthi', age=20):
    print(name)
    print(age)


details()

details('Deekshitha', 20)


# 9. Variable-Length Positional Arguments - *args

def display(*details):
    print(details)


display('Keerthi', 20)
display(10, 20, 30, 40)
display(10, 20, 30)


# 10. Keyword-Only Parameters - *

def details(name, *, salary, exp):
    print(name, salary, exp)


details('Keerthi', salary=25000, exp=10)


# 11. Positional-Only Parameters - /

def details(name, age, /):
    print(name, age)


details('Keerthi', 20)


# 12. Variable-Length Keyword Arguments - **kwargs

def details(**data):
    print(data)


details(name='Keerthi', age=20, course='Python')


# 13. Using *args and **kwargs

def details(*args, **kwargs):
    print(args)
    print(kwargs)


details(10, 20, 30, name='Keerthi', course='Python')
