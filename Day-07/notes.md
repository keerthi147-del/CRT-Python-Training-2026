# Day-07 – CRT Python Training
## Topics Covered

- Grouping Statements
- Iterative Statements
- for Loop
- while Loop
- range() Function
- Looping Through Strings
- Dictionary
- Collection Related Data Types

---

# Grouping Statements / Iterative Statements

If we require to execute a block of statements a limited number of times or an unlimited number of times, then we need to use iterative statements.

Iterative statements in Python are:

1. for loop
2. while loop

---

# for Loop

A for loop in Python is used to iterate through a sequence such as:

- List
- Tuple
- Dictionary
- String

We can also use range() for iteration.

## Basic Syntax

    for temp_var in sequence:
        # code to execute

## Example

    for i in range(5):
        print(i, end=' ')

### Output

    0 1 2 3 4

---

# range() Function

The range() function is used to generate a sequence of numbers.

## Syntax

    range(start, stop, step)

- start represents the starting value.
- stop represents the ending value.
- The stop value is not included.
- step represents the increment or decrement value.

---

## Case 1: range(stop)

    for i in range(5):
        print(i, end=' ')

### Output

    0 1 2 3 4

---

## Case 2: Another range() Example

    for i in range(7):
        print(i, end=' ')

### Output

    0 1 2 3 4 5 6

---

## Case 3: range(start, stop, step)

    for i in range(1, 10, 2):
        print(i, end=' ')

### Output

    1 3 5 7 9

---

## Case 4: Reverse Order

    for i in range(10, 0, -1):
        print(i, end=' ')

### Output

    10 9 8 7 6 5 4 3 2 1

---

# Looping Through a String

A for loop can be used to iterate through every character in a string.

## Syntax

    for ch in 'Python':
        print(ch)

### Output

    P
    y
    t
    h
    o
    n

---

# Dictionary

Dictionary is a collection-related data type in Python.

A dictionary contains multiple items.

Dictionary elements are stored as key-value pairs.

## Example

    student = {
        'name': 'Keerthi',
        'id': 122,
        'marks': 789,
        'per': 78.9
    }

We can use items() to access dictionary items.

## Example

    for key in student.items():
        print(key)

---

# Collection Related Data Types

Python has collection-related data types that can store multiple values.

Examples include:

- List
- Tuple
- Set
- Dictionary

Different collection-related data types have different characteristics.

---

# while Loop

If we require to execute a block of statements an unlimited number of times, we can use a while loop.

A while loop is generally used when the number of executions is not fixed.

For a limited number of executions, we can use increment or decrement operations.

## Basic Syntax

    while condition:
        # code to execute

---

## Example 1

    n = 1

    while n <= 5:
        print(n)

### Output

    1
    1
    1
    ...

The value of n must be updated to avoid an infinite loop.

---

## Example 2

    n = 1

    while n <= 5:
        print(n)
        n += 1

### Output

    1
    2
    3
    4
    5

---

# Infinite while Loop

An infinite while loop keeps executing continuously.

## Example

    while True:
        n = int(input('Enter a number: '))
        print(n)

The loop continues because the condition True always remains true.

---

# Summary

Today, I learned about:

- Grouping statements
- Iterative statements
- for loop
- while loop
- range() function
- range with start, stop and step values
- Forward iteration
- Reverse iteration
- Looping through strings
- Dictionary
- Collection-related data types
- Infinite while loops

These concepts are useful for repeating statements and iterating through sequences and collections in Python.
