# CRT Python Training - Day 05
# Date: 4 September 2026

# ============================================================
# READING INPUT VALUES
# ============================================================

# 1. Using multiple input()

a = int(input('Enter first integer: '))
b = int(input('Enter second integer: '))
c = int(input('Enter third integer: '))

print(a)
print(b)
print(c)


# 2. Using map() to read multiple values in a single line

a, b, c = map(int, input('Enter 3 int values: ').split())

print(a)
print(b)
print(c)


# 3. Using list() to read n number of elements

list1 = list(map(float, input('Enter n float elements: ').split()))

print(list1)
print(list1[0])
print(list1[1])

for i in list1:
    print(i)


# ============================================================
# OPERATORS IN PYTHON
# ============================================================

# 4. Arithmetic operators

a = 10
b = 20

print(a + b)
print(a - b)
print(a * b)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)


# 5. Comparison operators

a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


# 6. Logical operators

ctime = 9

print(ctime < 9 or ctime == 9)
print(ctime < 8 and ctime > 9)
print(not ctime > 4)


# 7. Assignment operators

a = 10

a += 1
print(a)

a *= 3
print(a)

a -= 3
print(a)

a //= 2
print(a)


# 8. Bitwise operators

a = 5
b = 3

print(a | b)
print(a & b)
print(a ^ b)
print(~a)
print(a << 2)


# 9. Membership operators

letters = ['aa', 'bb', 'cc']

print('aa' in letters)
print('cc' in letters)
print('kk' in letters)
print('pp' not in letters)


# 10. Identity operators

a = 10
b = a

print(a is b)


a = [1, 2]
b = a
c = [1, 2]

print(a is b)
print(a is c)
print(a is not c)
print(b is not c)


# 11. Ternary operator

age = 20

print('Eligible for vote' if age >= 18 else 'Not eligible')


# ============================================================
# STRING PROGRAMS USING OPERATORS
# ============================================================

# 12. Count the number of characters in a string

text = 'programming'
count = 0

for i in text:
    count += 1

print(count)


# 13. Count the number of vowels

text = 'programming'
count = 0

for i in text:
    if i in 'aeiou':
        count += 1

print(count)


# 14. Count vowels in uppercase or lowercase

text = 'prOGramming'
count = 0

for i in text:
    if i in 'aeiouAEIOU':
        count += 1

print(count)


# 15. Count the number of consonants

text = 'programming'
count = 0

for i in text:
    if i.isalpha() and i.lower() not in 'aeiou':
        count += 1

print(count)


# 16. Using isalpha()

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


# 17. Read a string in lowercase

name = input('Enter your name: ').lower()
print(name)


# 18. Convert string into lowercase after reading

name = input('Enter your name: ')
print(name.lower())


# 19. Convert string into uppercase

name = input('Enter your name: ').upper()
print(name)


# 20. Check whether the given string is lowercase or not

text = 'programminG'

if text.islower():
    print('String is in lower case')
else:
    print('String is not in lower case.')


# 21. Check whether string contains only alphabets
#     and is in lowercase

text = 'programming'

if text.isalpha() and text.islower():
    print('String is in lower case and contains only alphabets')
else:
    print('not in lower case and contains mixed')


# 22. Count uppercase and lowercase letters

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


# 23. Count the number of digits in a string

s = 'programming1234'
count = 0

for i in s:
    if i.isdigit():
        count += 1

print(count)


# ============================================================
# DAY 05 TASK / HOMEWORK
# ============================================================

# Program to read 3 different strings and:
# 1. Count the number of characters in the three strings.
# 2. Check whether the three strings are lowercase or uppercase.
# 3. Count uppercase letters.
# 4. Count lowercase letters.
# 5. Count digits.
# 6. Print lowercase letters.
# 7. Print uppercase letters.
# 8. Print digits.

# TODO: Complete this task as homework.
