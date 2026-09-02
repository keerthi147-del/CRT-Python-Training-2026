# CRT Python Training - Day 02

**Date:** 1 September 2026

## Topics Covered

### 1. print() Function

The `print()` function is used to display output in Python.

Example: `print("Hello, Python!")`

### 2. sep Attribute

The `sep` attribute is used to specify the separator between multiple values in the `print()` function.

The default value of `sep` is a space.

Example: `print("a", "b", "c", sep="*")`

Output: `a*b*c`

The separator can be changed according to the requirement.

### 3. end Attribute

The `end` attribute specifies what should be printed at the end of the output.

The default value of `end` is a newline (`\n`).

Example: `print("a", end="*")`

Using `end="*"` prints the next output on the same line with `*` between them.

### 4. Printing Using Multiple print() Statements

The `end` attribute can be used to print characters continuously on the same line.

Example:

`print("I", end="-")`  
`print("N", end="-")`  
`print("D", end="-")`  
`print("I", end="-")`  
`print("A")`

Output: `I-N-D-I-A`

### 5. for Loop with a String

A `for` loop can be used to access the characters of a string one by one.

Example:

`name = "keerthi"`  
`for temp in name:`  
`    print(temp, end=" ")`

Output: `k e e r t h i`

### 6. Python Data Types

Python supports different types of values.

- `str` - String values, such as `"India"`
- `int` - Integer values, such as `12`, `27`
- `float` - Floating-point values, such as `14.3`, `7.12`
- `complex` - Complex values, such as `10+4j`, `27+12j`
- `bool` - Boolean values, such as `True` and `False`

### 7. Boolean Values

Boolean values are represented by `True` and `False`.

`True` represents 1 and `False` represents 0.

Example: `print(True + True)`

Output: `2`

Boolean values must begin with a capital letter.

### 8. Complex Values

A complex number contains a real part and an imaginary part.

Example: `c = 10 + 4j`

Here:

- Real part = `10.0`
- Imaginary part = `4.0`

Python uses `j` to represent the imaginary part of a complex number.

The real and imaginary parts can be accessed using `.real` and `.imag`.

Example:

`c = 3.4 + 5.6j`  
`print(c)`  
`print(c.real)`  
`print(c.imag)`

Output:

`(3.4+5.6j)`  
`3.4`  
`5.6`

### Key Points

- `print()` is used to display output.
- `sep` specifies the separator between multiple values.
- The default value of `sep` is a space.
- `end` specifies what is printed at the end of the output.
- The default value of `end` is a newline.
- `sep` and `end` values can be changed according to the requirement.
- A `for` loop can be used to access characters of a string one by one.
- Python supports `str`, `int`, `float`, `complex`, and `bool` data types.
- Complex values have real and imaginary parts.
- `.real` returns the real part of a complex number.
- `.imag` returns the imaginary part of a complex number.
