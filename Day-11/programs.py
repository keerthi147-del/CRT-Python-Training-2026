# CRT Python Training - Day 11

# Date: 12 September 2026

# Topic: Functions


# 1. Function without arguments
def addition():
    a, b = map(int, input('Enter two values: ').split())
    print(a + b)


# 2. Function with multiple statements
def sub():
    print('Computer Networks')
    print('OOP')
    print('OS')
    print('FLAT')
    print('DBMS')


# 3. Function to initialize and print values
def m1():
    a, b, c, d = 10, 20, 30, 40
    print(a, b, c, d)


# 4. Function to read list elements and print them
def m2():
    values = list(map(int, input('Enter the list elements: ').split()))
    for i in values:
        print(i)


# 5. Function to read string values and print them
def m3():
    a, b, c, d = input('Enter the string values: ').split()
    print(f'a: {a}, b: {b}, c: {c}, d: {d}')


# 6. Function to print values using multiple statements
def m4():
    print('pen')
    print('pencil')


# 7. Function with multiple statements
def m5():
    print('Black')
    print('Blue')


# 8. Function with multiple statements
def m6():
    print('Red')
    print('Green')


# 9. Function with multiple statements
def m7():
    print('Morning')
    print('Night')


# 10. Calling a function
def cse():
    print('CSE')


# Function call
cse()


# 11. Calling a function multiple times
def fun():
    print('Python')


fun()
fun()
fun()


# 12. Function to print subject names
def subjects():
    print('Computer Networks')
    print('OOP')
    print('OS')
    print('FLAT')
    print('DBMS')


subjects()


# 13. Function with arguments
def f1(a, b):
    print(a + b)


f1(10, 20)


# 14. Function with three positional arguments
def f2(a, b, c):
    print(a, b, c)


f2(10, 20, 30)


# 15. Passing variables as arguments
a = 10
b = 20

f1(a, b)


# 16. Passing expressions as arguments
a = 8
b = 11

f1(a + 10, b + 20)


# 17. Function called with different argument values
def sum_values(a, b):
    print(a + b)


sum_values(10, 20)
sum_values(20, 40)


# 18. Function with positional arguments
def positional(a, b, c):
    print(a, b, c)


positional(10, 20, 30)


# 19. Function with no statements using pass
def empty_function():
    pass


# Calling the empty function
empty_function()
