## 🐍 programs.py

# Day 10 – CRT Python Training

# Dictionary and Functions

# -----------------------------------
# 1. Creating an Empty Dictionary
# -----------------------------------

dict_var = {}

print(dict_var)


# -----------------------------------
# 2. Creating an Empty Dictionary Using dict()
# -----------------------------------

dict_var = dict()

print(dict_var)


# -----------------------------------
# 3. Initializing a Dictionary
# -----------------------------------

student = {
    'name': 'Keerthi',
    'id': 122,
    'college': 'Vignan',
    'course': 'Python'
}

print(student)


# -----------------------------------
# 4. Accessing Dictionary Elements
# -----------------------------------

student = {
    'name': 'Keerthi',
    'id': 122,
    'college': 'Vignan'
}

print(student['name'])
print(student['id'])
print(student['college'])


# -----------------------------------
# 5. Dictionary keys() Method
# -----------------------------------

dict_var = {
    'laptop': 32000,
    'mobile': 20000,
    'brand': 'Samsung'
}

print(dict_var.keys())


# -----------------------------------
# 6. Dictionary values() Method
# -----------------------------------

dict_var = {
    'laptop': 32000,
    'mobile': 20000,
    'brand': 'Samsung'
}

print(dict_var.values())


# -----------------------------------
# 7. Dictionary items() Method
# -----------------------------------

dict_var = {
    'laptop': 32000,
    'mobile': 20000,
    'brand': 'Samsung'
}

print(dict_var.items())


# -----------------------------------
# 8. Accessing Keys Using for Loop
# -----------------------------------

dict_var = {
    'laptop': 32000,
    'mobile': 20000,
    'brand': 'Samsung'
}

for key in dict_var.keys():
    print(key)


# -----------------------------------
# 9. Accessing Values Using for Loop
# -----------------------------------

dict_var = {
    'laptop': 32000,
    'mobile': 20000,
    'brand': 'Samsung'
}

for value in dict_var.values():
    print(value)


# -----------------------------------
# 10. Accessing Keys and Values Using for Loop
# -----------------------------------

dict_var = {
    'laptop': 32000,
    'mobile': 20000,
    'brand': 'Samsung'
}

for key, value in dict_var.items():
    print(key, value)


# -----------------------------------
# 11. Using zip() Function
# -----------------------------------

a = [10, 20, 30]
b = ['Keerthi', 'Mobile', 'Samsung']

result = zip(a, b)

print(list(result))


# -----------------------------------
# 12. Using dict() and zip()
# -----------------------------------

keys = ['laptop', 'mobile', 'brand']
values = [32000, 20000, 'Samsung']

result = dict(zip(keys, values))

print(result)


# -----------------------------------
# 13. Finding Minimum Value Using min()
# -----------------------------------

numbers = [3, 7, 2, 9, 5]

minimum = min(numbers)

print(minimum)


# -----------------------------------
# 14. Finding Maximum Value Using max()
# -----------------------------------

numbers = [3, 7, 2, 9, 5]

maximum = max(numbers)

print(maximum)


# -----------------------------------
# 15. Simple Function
# -----------------------------------

def display():
    print('Welcome to Python')


display()


# -----------------------------------
# 16. Function with Arguments
# -----------------------------------

def addition(a, b):
    result = a + b
    print(result)


addition(10, 20)


# -----------------------------------
# 17. Function with Return Value
# -----------------------------------

def addition(a, b):
    result = a + b
    return result


answer = addition(10, 20)

print(answer)


# -----------------------------------
# 18. Function Called Multiple Times
# -----------------------------------

def greet():
    print('Hello, welcome to Python')


greet()
greet()
greet()


# -----------------------------------
# 19. Function to Find Minimum Value
# -----------------------------------

def find_minimum(numbers):
    print(min(numbers))


numbers = [10, 25, 5, 40, 15]

find_minimum(numbers)


# -----------------------------------
# 20. Function to Find Maximum Value
# -----------------------------------

def find_maximum(numbers):
    print(max(numbers))


numbers = [10, 25, 5, 40, 15]

find_maximum(numbers)
