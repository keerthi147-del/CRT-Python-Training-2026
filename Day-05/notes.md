# CRT Python Training - Day 05
# Date: 4 September 2026

## Reading Input Values from User

Python provides different ways to read values from the user.

### 1. Using Multiple input()

Multiple values can be read using separate input() functions.

Example:

    a = int(input())
    b = int(input())
    c = int(input())

Here, each value is read separately.

### 2. Using map()

map() can be used to read multiple values in a single line.

Syntax:

    map(conversion_method, sequence_of_values)

Example:

    a, b, c = map(int, input('Enter 3 int values').split())

Here:
- input() reads the values as a string.
- split() separates the values.
- map() applies the conversion method to each value.
- int converts the values into integers.

### 3. Using list()

list() can be used to read n number of elements.

Example:

    list1 = list(map(float, input('Enter n float elements').split()))

    print(list1)
    print(list1[0])
    print(list1[1])

A for loop can also be used to print each element:

    for i in list1:
        print(i)

---

# Operators in Python

Operators are symbols or keywords used to perform operations on variables or values.

## Types of Operators in Python

### 1. Arithmetic Operators

Arithmetic operators are used for mathematical calculations.

Operators:

    +, -, *, /, //, %, **

Example:

    a = 10
    b = 20
    c = a + b

Important arithmetic operators:

- + : Addition
- - : Subtraction
- * : Multiplication
- / : Division
- // : Floor division
- % : Modulus
- ** : Exponentiation

Example:

    print(a + b)
    print(a - b)
    print(a * b)
    print(10 / 3)
    print(10 // 3)
    print(10 % 3)
    print(10 ** 3)

### 2. Comparison Operators

Comparison operators are used to compare two values.

They return either True or False.

Operators:

    ==, !=, <, >, <=, >=

Example:

    a = 10
    b = 20

    print(a == b)
    print(a != b)
    print(a > b)
    print(a < b)
    print(a >= b)
    print(a <= b)

Comparison operators are commonly used with:

- if
- if-else
- else-if
- nested if
- multiple if conditions

### 3. Logical Operators

Logical operators are used to combine conditions.

Operators:

    and
    or
    not

Example:

    a, b = 10, 20

    print(a == 10 and b == 20)

Here:
- a == 10 is condition-1.
- b == 20 is condition-2.
- and combines both conditions.

Another example:

    ctime = 9

    print(ctime < 9 or ctime == 9)
    print(ctime < 8 and ctime > 9)
    print(not ctime > 4)

### 4. Assignment Operators

Assignment operators are used to assign or update values.

Operators include:

    =
    +=
    -=
    *=
    /= 
    //=

Example:

    a = 10
    a += 2
    print(a)

The statement:

    a += 2

is equivalent to:

    a = a + 2

Other examples:

    a = 10
    a += 1
    a *= 3
    a -= 3
    a //= 2

### 5. Bitwise Operators

Bitwise operators operate on individual bits of integers.

The bits are:

    0 and 1

Operators include:

    &
    |
    ^
    ~
    <<
    >>

Example:

    a = 5
    b = 3

Binary representation:

    5 = 0101
    3 = 0011

#### Bitwise OR (|)

OR returns 1 if at least one of the corresponding bits is 1.

    0101
    0011
    ----
    0111

Therefore:

    print(a | b)

Output:

    7

#### Bitwise AND (&)

AND returns 1 only when both corresponding bits are 1.

    0101
    0011
    ----
    0001

Therefore:

    print(a & b)

Output:

    1

#### Bitwise XOR (^)

XOR means Exclusive OR.

It returns 1 when the two bits are different.

Rules:

    0 0 -> 0
    0 1 -> 1
    1 0 -> 1
    1 1 -> 0

Example:

    0101
    0011
    ----
    0110

Therefore:

    print(a ^ b)

Output:

    6

#### Bitwise NOT (~)

Bitwise NOT changes 0 to 1 and 1 to 0.

Example:

    a = 5

The shortcut formula is:

    ~a = -(a + 1)

Therefore:

    ~5 = -(5 + 1)
       = -6

Similarly:

    ~10 = -(10 + 1)
         = -11

#### Left Shift (<<)

Left shift can be represented as:

    a << n = a * 2^n

---

### 6. Membership Operators

Membership operators are used to check whether a value exists in a sequence.

Operators:

    in
    not in

Example:

    letters = ['aa', 'bb', 'cc']

    print('aa' in letters)
    print('cc' in letters)
    print('kk' in letters)
    print('pp' not in letters)

At least one value and a sequence of elements are required.

### 7. Identity Operators

Identity operators are used to check whether two variables refer to the same object.

Operators:

    is
    is not

Example:

    a = 10
    b = a

    print(a is b)

For lists:

    a = [1, 2]
    b = a
    c = [1, 2]

    print(a is b)
    print(a is c)
    print(a is not c)
    print(b is not c)

Here, identity checks whether variables refer to the same object.

### 8. Ternary / Conditional Operator

The ternary operator provides a short way to write an if-else statement.

Syntax:

    x if condition else y

Example:

    age = 20

    print('Eligible for vote' if age >= 18 else 'Not eligible')

---

# Quick Revision

### Arithmetic

    +, -, *, /, //, %, **

### Comparison

    ==, !=, <, >, <=, >=

### Logical

    and, or, not

### Assignment

    =, +=, -=, *=, /=, //=

### Bitwise

    &, |, ^, ~, <<, >>

### Membership

    in, not in

### Identity

    is, is not

### Ternary

    x if condition else y

---

# String Programs Using Operators

## 1. Count the Number of Characters in a String

Example:

    text = 'programming'
    count = 0

    for i in text:
        count += 1

    print(count)

## 2. Count the Number of Vowels

Example:

    text = 'programming'
    count = 0

    for i in text:
        if i in 'aeiou':
            count += 1

    print(count)

Output:

    3

## 3. Count Vowels in Uppercase or Lowercase

Example:

    text = 'prOGramming'
    count = 0

    for i in text:
        if i in 'aeiouAEIOU':
            count += 1

    print(count)

Output:

    3

## 4. Count the Number of Consonants

Example:

    text = 'programming'
    count = 0

    for i in text:
        if i.isalpha() and i not in 'aeiou':
            count += 1

    print(count)

For the string 'programming', the output is:

    8

---

# isalpha()

isalpha() is used to check whether a string contains only alphabetic characters.

Syntax:

    string.isalpha()

Examples:

    a = 'hello'
    print(a.isalpha())

    b = 'python'
    print(b.isalpha())

    c = 'python123'
    print(c.isalpha())

    d = 'hello goodmorning'
    print(d.isalpha())

    e = 'namaste!'
    print(e.isalpha())

    print(' '.isalpha())

Results:

- 'hello' -> True
- 'python' -> True
- 'python123' -> False
- 'hello goodmorning' -> False
- 'namaste!' -> False
- ' ' -> False

---

# lower() and upper()

The lower() function is used to convert a string into lowercase.

Syntax:

    string.lower()

A string can be converted into lowercase while reading input:

    name = input('Enter your name').lower()

Or it can be converted after reading:

    name = input('Enter your name')
    print(name.lower())

Similarly, upper() can be used to convert a string into uppercase.

Example:

    name = input('Enter your name ').upper()

---

# Checking Lowercase or Uppercase

A string can be checked using islower().

Example:

    text = 'programminG'

    if text.islower():
        print('String is in lower case')
    else:
        print('String is not in lower case.')

---

# Checking Alphabet and Lowercase

A string can be checked using isalpha() and islower() together.

Example:

    text = 'programming'

    if text.isalpha() and text.islower():
        print('String is in lower case and contains only alphabets')
    else:
        print('not in lower case and contains mixed')

---

# Counting Uppercase and Lowercase Letters

Example:

    s = 'ProGramminG'

    upper_c = 0
    lower_c = 0

    for i in s:
        if i.isupper():
            upper_c += 1
        elif i.islower():
            lower_c += 1

    print('uppercase_c', upper_c)
    print('lowercase_c', lower_c)

---

# Counting Digits in a String

isdigit() can be used to check whether a character is a digit.

Example:

    s = 'programming1234'
    count = 0

    for i in s:
        if i.isdigit():
            count += 1

    print(count)

Output:

    4

---

# Task for the Day

Program to read 3 different strings and:

1. Count the number of characters in the three strings.
2. Check whether the three strings are in lowercase or uppercase.
3. Count the number of uppercase letters.
4. Count the number of lowercase letters.
5. Count the number of digits.
6. Print lowercase letters.
7. Print uppercase letters.
8. Print digits.
