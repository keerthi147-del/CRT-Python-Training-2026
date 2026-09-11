# Day 10 – CRT Python Training

## Dictionary

- It is also an in-built Python data structure.
- The elements in a dictionary data structure should be in key-value pairs.

### Creating an Empty Dictionary Variable

We can create an empty dictionary variable by using the predefined symbol `{}`.

Syntax:

dict_var = {}

We can also create an empty dictionary using the `dict()` function.

Syntax:

dict_var = dict()

---

## Initialization of Dictionary Variable

We can directly initialize elements to a dictionary variable at a time, which is known as initialization.

Syntax:

dict_var = {key1: value1, key2: value2, ...}

Example:

d = {'laptop': 30000, 'mobile': 20000, 'brand': 'Samsung'}

---

## Accessing Dictionary Variable Elements

To access any individual value of a dictionary variable, we need to use the name of the key.

Example:

d = {'laptop': 30000, 'mobile': 20000, 'brand': 'Samsung'}

print(d['laptop'])

Output:

30000

---

## Dictionary Methods

### dict.values()

Used to print dictionary values.

Syntax:

print(dict_var.values())

### dict.keys()

Used to print dictionary keys.

Syntax:

print(dict_var.keys())

### dict.items()

Used to print dictionary key-value pairs.

Syntax:

print(dict_var.items())

---

## Adding Key-Value Pairs

Syntax:

dict_var['key'] = value

Example:

d = {}

d['laptop'] = 30000
d['mobile'] = 20000

print(d)

---

## Updating Dictionary Values

We can update dictionary values by using the corresponding key.

Syntax:

dict_var['key'] = value

Example:

d = {'laptop': 30000, 'mobile': 20000, 'brand': 'Samsung'}

d['mobile'] = 25000

print(d)

---

# zip()

It is a predefined function used to combine two iterables as a group.

Example:

a = [10]
b = ['Keerthi']

z = zip(a, b)

print(z)

---

## Creating a Dictionary Using zip()

Example:

keys = ['laptop', 'mobile', 'brand']

values = [30000, 20000, 'Samsung']

d = dict(zip(keys, values))

print(d)

---

# List Operations

## min()

Used to find the minimum element in a list.

Example:

l = [3, 1, 9, 6, 5]

print(min(l))

---

## max()

Used to find the maximum element in a list.

Example:

l = [3, 1, 9, 6, 5]

print(max(l))

---

## Finding Minimum Without Using min()

Example:

l = [3, 1, 9, 6, 5]

min = l[0]

for i in l:
    if i < min:
        min = i

print(min)

---

## Finding Maximum Without Using max()

Example:

l = [3, 1, 9, 6, 5]

max = l[0]

for i in l:
    if i > max:
        max = i

print(max)

---

# Functions

A function is a grouped/block of code statements used to perform a specific task.

A function can contain multiple statements.

## Types of Functions

- Predefined functions
- User-defined functions

---

## Predefined Functions

Examples:

print()
len()
min()
max()

---

## User-Defined Functions

A user-defined function is created by the programmer to perform a specific task.

Syntax:

def function_name():
    statements

---

## Calling a Function

To execute a function, we need to call the function by using its name.

Example:

def add():
    print('Hello')

add()

We can call a function n number of times.

Example:

def add():
    print('Hello')

add()
add()
add()
