# CRT Python Training - Day 03

**Date:** 2 September 2026  
**Training Day:** 3 / 20

## Topics Covered

Today’s session focused on Python strings, indexing, slicing, negative indexing, loops, and different ways of accessing, reversing, and copying strings.

## 1. String Indexing

A string is a sequence of characters, and each character is assigned an index.

For example:

    name = 'Keerthi'

### Positive Indexing

Positive indexing starts from `0` from the left side.

    K   e   e   r   t   h   i
    0   1   2   3   4   5   6

### Negative Indexing

Negative indexing starts from `-1` from the right side.

    K    e    e    r    t    h    i
    -7  -6   -5   -4   -3   -2   -1

## 2. String Slicing

String slicing is used to access a part of a string.

### Syntax

    string[start:stop:step]

The `start`, `stop`, and `step` values determine which characters are accessed.

Example:

    name = 'Keerthi'
    print(name[0:4])
    print(name[:4])
    print(name[::-1])

## 3. Negative Slicing

Negative indexes can also be used with slicing.

Example:

    name = 'india'
    print(name[:-1])

Output:

    indi

Here, `-1` represents the last character, so `[:-1]` accesses all characters before the last character.

## 4. Reversing a String

A string can be reversed using slicing.

Example:

    name = 'Keerthi'
    print(name[::-1])

A string can also be reversed using a `for` loop.

Example:

    name = 'Keerthi'
    new_name = ""

    for i in name:
        new_name = i + new_name

    print(new_name)

Both methods can be used to reverse a string.

## 5. Accessing Alternative Characters

Alternative characters of a string can be accessed using a `for` loop and `range()`.

Example:

    name = 'Prathima'

    for i in range(0, len(name), 2):
        print(name[i])

Here, the step value `2` is used to access alternate positions.

## 6. Finding the Index of Each Character

The index and character of each character in a string can be displayed using a counter.

Example:

    name = 'india'
    count = 0

    for i in name:
        print(count, ":", i)
        count = count + 1

Output:

    0 : i
    1 : n
    2 : d
    3 : i
    4 : a

### Using enumerate()

Another easier method is using the `enumerate()` function.

Example:

    name = "india"

    for i, char in enumerate(name):
        print(i, ":", char)

This provides both the index and the character during iteration.

## 7. Copying a String

A string can be copied in different ways.

### Method 1: Direct Assignment

    name = 'Keerthi'
    new_name = name
    print(new_name)

### Method 2: Using Slicing

    name = 'Keerthi'
    new_name = name[:]
    print(new_name)

### Method 3: Using a for Loop

    name = 'Keerthi'
    new_name = ''

    for i in name:
        new_name = new_name + i

    print(new_name)

## Lab Practice

During today’s session, I practiced and executed the following programs:

1. Program to print a complete string in reverse using slicing.
2. Program to print the last 5 characters of a string using negative slicing.
3. Program to print all characters except the last 3 characters using negative slicing.
4. Program to print a string in reverse using different methods.
5. Program to print alternative characters of a string without using slicing.
6. Program to print the index of each character along with the character.
7. Program to copy a given string using different methods.

All the above programs were executed successfully using Python through Command Prompt.

## Homework / Additional Practice

The following programs were assigned as homework:

1. Using a `for` loop, print each character of a given string.

2. Count the number of characters in a string without using `len()`.

3. Print the first 4 characters of the given string using negative slicing.

4. Initialize four different strings such as name, college name, course name, and native place. Print the first two strings using the `range()` method and print the next two strings using the `in` sequence.

## Key Takeaways

- A string is a sequence of characters.
- Python supports both positive and negative indexing.
- Positive indexing starts from `0`.
- Negative indexing starts from `-1`.
- Slicing can be used to access a portion of a string.
- The general slicing syntax is `string[start:stop:step]`.
- `[::-1]` can be used to reverse a string.
- `for` loops can be used to process characters one by one.
- `range()` can be used with indexes to access characters.
- `enumerate()` provides both the index and character while iterating.
- Alternative characters can be accessed using a suitable step value.
- A string can be copied using direct assignment, slicing, or a loop.

## Reflection

Today’s session helped me understand Python strings more clearly through indexing and slicing. I practiced positive and negative indexing and learned different ways to reverse, access, count, and copy strings.

The lab session was especially useful because I was able to write and execute the programs myself using Python in Command Prompt. Practicing these concepts helped me understand strings and loops better and gave me a stronger foundation for solving Python problems.

## Progress

**CRT Python Training — Day 03 / 20**

**Learn • Practice • Grow 🌱**
