#🐍 programs.py
# ==========================================
# DAY-07 – CRT PYTHON TRAINING
# Topics:
# for Loop, while Loop, range(), Strings
# and Dictionary
# ==========================================


# ------------------------------------------
# PROGRAM 1: Basic for Loop
# ------------------------------------------

for i in range(5):
    print(i, end=' ')


# ------------------------------------------
# PROGRAM 2: for Loop with a Tuple
# ------------------------------------------

print()

text = ('a', 'b', 'c')

for item in text:
    print(item, end=' ')


# ------------------------------------------
# PROGRAM 3: range(5)
# ------------------------------------------

print()

for i in range(5):
    print(i, end=' ')


# Output: 0 1 2 3 4


# ------------------------------------------
# PROGRAM 4: range(7)
# ------------------------------------------

print()

for i in range(7):
    print(i, end=' ')


# Output: 0 1 2 3 4 5 6


# ------------------------------------------
# PROGRAM 5: range() with Step Value
# ------------------------------------------

print()

for i in range(1, 10, 2):
    print(i, end=' ')


# Output: 1 3 5 7 9


# ------------------------------------------
# PROGRAM 6: range() in Reverse Order
# ------------------------------------------

print()

for i in range(10, 0, -1):
    print(i, end=' ')


# Output: 10 9 8 7 6 5 4 3 2 1


# ------------------------------------------
# PROGRAM 7: Loop Through a String
# ------------------------------------------

print()

text = 'Python'

for ch in text:
    print(ch)


# ------------------------------------------
# PROGRAM 8: Dictionary
# ------------------------------------------

student = {
    'name': 'Keerthi',
    'id': 122,
    'marks': 789,
    'per': 78.9
}

for key, value in student.items():
    print(key, ':', value)


# ------------------------------------------
# PROGRAM 9: Basic while Loop
# ------------------------------------------

n = 1

while n <= 5:
    print(n)
    n += 1


# ------------------------------------------
# PROGRAM 10: Infinite while Loop
# ------------------------------------------

# Uncomment the below code to run

# while True:
#     n = int(input('Enter a number: '))
#     print(n)


# ------------------------------------------
# PROGRAM 11: Multiplication Table
# ------------------------------------------

n = int(input('Enter a number: '))

for i in range(1, 11):
    print(n, 'x', i, '=', n * i)


# ==========================================
# END OF DAY-07 PROGRAMS
# ==========================================
