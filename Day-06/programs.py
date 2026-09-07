# Day-06/programs.py

#CONTROL STATEMENTS
# Date: 7 September 2026


# ==================================================
# 1. PROGRAM TO CHECK WHETHER A PERSON IS ELIGIBLE TO VOTE
# ==================================================

age = int(input('Enter your age: '))

if age >= 18:
    print('You are eligible to vote')


# ==================================================
# 2. PROGRAM TO CHECK WHETHER A NUMBER IS POSITIVE OR NEGATIVE
# ==================================================

value = int(input('Enter a value to check: '))

if value >= 0:
    print('Positive number')


# ==================================================
# 3. PROGRAM TO CHECK WHETHER A NUMBER IS EVEN OR ODD
# ==================================================

value = int(input('Enter a value to check: '))

if value % 2 == 0:
    print(f'{value} is even')


# ==================================================
# 4. PROGRAM USING IF-ELSE TO CHECK VOTING ELIGIBILITY
# ==================================================

age = int(input('Enter your age: '))

if age >= 18:
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')


# ==================================================
# 5. PROGRAM TO CHECK WHETHER A NUMBER IS POSITIVE, NEGATIVE OR ZERO
# ==================================================

value = int(input('Enter the value: '))

if value > 0:
    print('Positive')
elif value < 0:
    print('Negative')
else:
    print('Zero')


# ==================================================
# 6. PROGRAM TO CHECK WHETHER A NUMBER IS EVEN OR ODD
# ==================================================

value = int(input('Enter a value to check: '))

if value % 2 == 0:
    print(f'{value} is even')
else:
    print(f'{value} is odd')


# ==================================================
# 7. PROGRAM TO CHECK BANK ACCOUNT ACCESS
# ==================================================

account = int(input('Enter your account number: '))

if account == 1237:
    print('Welcome to your account')
else:
    print('Invalid account number')


# ==================================================
# 8. PROGRAM USING MATCH-CASE
# ==================================================

option = int(input('Enter an option: '))

match option:
    case 1:
        print('Option 1 selected')

    case 2:
        print('Option 2 selected')

    case 3:
        print('Option 3 selected')

    case _:
        print('Invalid option')
