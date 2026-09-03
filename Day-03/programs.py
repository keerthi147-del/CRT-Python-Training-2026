# CRT Python Training - Day 03
# Date: 2 September 2026

# ============================================================
# LAB PROGRAMS
# ============================================================

# 1. Program to print complete string in reverse using slice

name = 'Keerthi'
print(name[::-1])


# 2. Program to print the last 5 characters of the string
#    using negative slice

name = 'My family is YAPTK'
print(name[-5:])


# 3. Program to print all characters except the last
#    3 characters using negative slice

name = 'Keerthi chowdhary Yeddurii..'
print(name[:-3])


# 4. Program to print the string in reverse
#    using different methods

name = 'Keerthi'

# Method 1: Using slicing
print(name[::-1])

print('OR')

# Method 2: Using for loop
n_name = ''

for i in name:
    n_name = i + n_name

print(n_name)


# 5. Program to print alternative characters of the
#    given string without using slice

name = 'Prathima'

for i in range(0, len(name), 2):
    print(name[i])


# 6. Program to print index of each character along
#    with the character of the given string

# Sample input: india
# Sample output:
# 0 : i
# 1 : n
# 2 : d
# 3 : i
# 4 : a

name = 'india'
count = 0

for i in name:
    print(count, ':', i)
    count = count + 1


print('-----Another Method(easy)-------')

s = 'india'

for i, char in enumerate(s):
    print(i, ':', char)


# 7. Program to copy the given string/text

name = 'Keerthi'

# Method 1: Direct assignment
n_name = name
print(n_name)

print('OR')

# Method 2: Using slice
ne_name = name[:]
print(ne_name)

print('OR')

# Method 3: Using for loop
new_name = ''

for i in name:
    new_name = new_name + i

print(new_name)


# ============================================================
# HOMEWORK PROGRAMS
# ============================================================

# 8. Using for loop - print each character of a given string

name = 'Keerthi'

for i in name:
    print(i, end=' ')

print()


# 9. Count the number of characters in a string
#    without using len()

name = 'Hyderabad'
count = 0

for i in name:
    count = count + 1

print(count)


# 10. Program to print the first 4 characters of the
#     given string using negative slicing

name = 'india'

print(name[:-1])


# 11. Initialize four different strings:
#     name, college name, course name and native place.
#     First two strings using range()
#     Next two strings using in sequence.

name = 'Keerthi'
college = "Vignan's Nirula"
course = 'Python'
native = 'Guntur'

# First string using range()
for i in range(len(name)):
    print(name[i], end=' ')

print()

# Second string using range()
for i in range(len(college)):
    print(college[i], end=' ')

print()

# Third string using in sequence
for i in course:
    print(i, end=' ')

print()

# Fourth string using in sequence
for i in native:
    print(i, end=' ')
