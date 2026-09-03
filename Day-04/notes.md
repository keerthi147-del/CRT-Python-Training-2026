# CRT Python Training - Day 04

**Date:** 3 September 2026

## Different Ways to Initialize Values in Python

In Python, we can initialize any type of value in multiple ways.

### In C Programming

#### Case 1: Direct Value Initialization

```c
int a = 10;
```

This is direct value initialization.

#### Case 2: Declaration and Initialization

```c
int a;
a = 10;
```

Here, the variable is first declared and then initialized.

### In Java

In Java, we have to initialize variables similar to C programming.

### In Python

In Python, we can initialize values in multiple ways.

### Case 1: Direct Initialization

Example:

```python
a = 10
b = 30
c = 50

print(a, b, c)
```

### Case 2: Multiple Values in Multiple Variables in a Single Line

Example:

```python
a, b, c = 10, 20, 30
```

**Note:** The number of values should be equal to the number of variables.

### Case 3: Multiple Values in a Single Variable

Multiple values can be stored in a single variable using a **list**.

Example:

```python
a = [10, 20, 30, 40]
```

Each value is stored at a separate index.

```text
Value :  10   20   30   40
Index :   0    1    2    3
```

```python
print(a)
```

Output:

```text
[10, 20, 30, 40]
```

### Case 4: Multiple Values in a Single Variable Using Tuple

Example:

```python
a = (10, 20, 30, 40)

print(a)
```

A tuple can store multiple values in a single variable.

### Case 5: Multiple Values in Multiple Variables

Example:

```python
a, b, c = 10, 20, 30

print(a, b, c)
```

### Case 6: Extended Sequence Unpacking

Example:

```python
a, *b = 'india'

print(a)
print(b)
```

Here, the first value is assigned to `a` and the remaining values are assigned to `b`.

---

# Different Ways to Print Any Value in Python

In C programming, format specifiers are used to print values.

Example:

```c
int a = 10;
printf("%d", a);
```

In Python, we can directly print the value.

```python
a = 10

print(a)
```

Python provides different ways to print values.

### Using `print()`

```python
a = 10
b = 20

print(a, b)
```

### Using f-string

```python
a = 10
b = 20

print(f'a={a} b={b}')
```

### Using `format()`

```python
a = 10
b = 20

print('a={} b={}'.format(a, b))
```

---

# Reading Input Values from User in Python

In Python, we can read values from the user using the `input()` function.

Example:

```python
a = input()

print(a)
```

We can also provide a message while taking input.

```python
name = input('Enter your name: ')

print(name)
```

### Important Point

The default type of the value received from `input()` is `str`.

Example:

```python
a = input()

print(type(a))
```

Even if the user enters a number such as:

```text
10
```

the value received by `input()` is a string.

---

# Reading Different Types of Values

In Java, we have predefined methods such as:

```text
nextInt()
nextFloat()
nextDouble()
next()
nextLine()
```

These methods are used to read different types of values.

In Python, we mainly use the `input()` function and convert the received value into the required type.

---

# Type Conversion

We can convert one type of value into another type using predefined functions.

Some commonly used conversion functions are:

```python
str()
int()
float()
complex()
bool()
```

### String to Integer

```python
a = '10'

a = int(a)

print(a)
```

### String to Float

```python
a = '10.5'

a = float(a)

print(a)
```

### String to Complex

```python
a = '10+2j'

a = complex(a)

print(a)
```

### Value to Boolean

```python
a = 10

a = bool(a)

print(a)
```

### Value to String

```python
a = 10

a = str(a)

print(a)
```

---

# Checking the Type of a Value

Python provides the `type()` function to find the type of a value.

Example:

```python
a = 'india'

print(type(a))
```

Output:

```text
<class 'str'>
```

Another example:

```python
a = 10

print(type(a))
```

Output:

```text
<class 'int'>
```

---

# Reading Input and Type Conversion Together

We can convert the input value while reading it.

### Integer Input

```python
a = int(input('Enter a number: '))

print(a)
```

### Float Input

```python
a = float(input('Enter a value: '))

print(a)
```

### Complex Input

```python
a = complex(input('Enter a complex value: '))

print(a)
```

### Boolean Input

```python
a = bool(input('Enter a value: '))

print(a)
```

---

# Important Point About `input()`

The `input()` function always reads the value as a string first.

Example:

```python
a = input('Enter a value: ')
```

If the user enters:

```text
10
```

Python receives it as:

```text
'10'
```

If we need it as an integer, we use:

```python
a = int(input('Enter a value: '))
```

---

# Formatted Strings

Python supports formatted strings for displaying values along with text.

### Using f-string

```python
a = 10
b = 20

print(f'a={a} b={b}')
```

The `f` before the string allows variables to be inserted directly inside `{}`.

### Using `format()`

```python
a = 10
b = 20

print('a={} b={}'.format(a, b))
```

The `format()` method replaces `{}` with the given values.

---

# Homework Assigned

The trainer also assigned the following programs as homework:

1. Program to read N number of elements and print them line by line.

2. Program to read 4 different types of values using a single line.

3. Program to initialize your name and print each character.

4. Program to read a friend's name and print each character.

5. Program to read 4 boolean values and print the first two.

6. Program to read N number of float values and print all the values.

7. Program to read N number of complex values and print all the values.

These homework programs will be completed separately and added to the repository after completion.

---

# Key Takeaways

- Python allows multiple ways to initialize values.
- Multiple variables can be initialized in a single line.
- Multiple values can be stored in a list or tuple.
- Python does not require explicit variable declaration before initialization.
- `print()` is used to display values.
- `input()` is used to read values from the user.
- The default type returned by `input()` is `str`.
- Type conversion can be performed using `int()`, `float()`, `complex()`, `bool()` and `str()`.
- `type()` is used to identify the type of a value.
- f-strings and `format()` can be used for formatted output.
- Python provides simple ways to work with different types of input values.
