
## 💻 `Day-04/programs.py`
# CRT Python Training - Day 04
# Date: 3 September 2026

# ============================================================
# DIFFERENT WAYS TO INITIALIZE VALUES
# ============================================================
# 1. Direct initialization

a = 10
b = 30
c = 50

print(a, b, c)


# 2. Multiple values in multiple variables in a single line

a, b, c = 10, 20, 30

print(a, b, c)


# 3. Multiple values in a single variable using list

a = [10, 20, 30, 40]

print(a)


# 4. Multiple values in a single variable using tuple

a = (10, 20, 30, 40)

print(a)


# 5. Multiple values in multiple variables

a, b, c = 10, 20, 30

print(a, b, c)


# 6. Extended sequence unpacking

a, *b = 'india'

print(a)
print(b)


# ============================================================
# DIFFERENT WAYS TO PRINT VALUES
# ============================================================

# 7. Using print() directly

a = 10
b = 20

print(a, b)


# 8. Using f-string

a = 10
b = 20

print(f'a={a} b={b}')


# 9. Using format()

a = 10
b = 20

print('a={} b={}'.format(a, b))


# ============================================================
# INPUT AND TYPE CONVERSION
# ============================================================

# 10. Reading a string value

name = input('Enter your name: ')
print(name)


# 11. Reading an integer value

a = int(input('Enter an integer: '))
print(a)


# 12. Reading a float value

a = float(input('Enter a float value: '))
print(a)


# 13. Reading a complex value

a = complex(input('Enter a complex value: '))
print(a)


# 14. Checking the type of a value

a = 'india'

print(type(a))


# 15. String to integer conversion

a = '10'
a = int(a)

print(a)
print(type(a))


# 16. String to float conversion

a = '10.5'
a = float(a)

print(a)
print(type(a))


# 17. String to complex conversion

a = '10+2j'
a = complex(a)

print(a)
print(type(a))


# 18. Value to boolean conversion

a = 10
a = bool(a)

print(a)
print(type(a))


# 19. Value to string conversion

a = 10
a = str(a)

print(a)
print(type(a))


# ============================================================
# FORMATTED OUTPUT
# ============================================================

# 20. Using f-string

a = 10
b = 20

print(f'a={a} b={b}')


# 21. Using format()

a = 10
b = 20

print('a={} b={}'.format(a, b))


# ============================================================
# HOMEWORK / PRACTICE PROGRAMS
# ============================================================

# 22. Program to read N number of elements and print them

n = int(input('Enter number of elements: '))

for i in range(n):
    value = input('Enter value: ')
    print(value)


# 23. Program to read 4 different types of values

a = int(input('Enter integer value: '))
b = float(input('Enter float value: '))
c = complex(input('Enter complex value: '))
d = input('Enter string value: ')

print(a)
print(b)
print(c)
print(d)


# 24. Program to initialize your name and print each character

name = 'Keerthi'

for i in name:
    print(i)


# 25. Program to read friend name and print each character

friend = input('Enter friend name: ')

for i in friend:
    print(i)


# 26. Program to read 4 boolean values and print the first two

a = bool(input('Enter first value: '))
b = bool(input('Enter second value: '))
c = bool(input('Enter third value: '))
d = bool(input('Enter fourth value: '))

print(a)
print(b)


# 27. Program to read N number of float values and print all values

n = int(input('Enter number of float values: '))

for i in range(n):
    value = float(input('Enter float value: '))
    print(value)


# 28. Program to read N number of complex values and print all values

n = int(input('Enter number of complex values: '))

for i in range(n):
    value = complex(input('Enter complex value: '))
    print(value)
