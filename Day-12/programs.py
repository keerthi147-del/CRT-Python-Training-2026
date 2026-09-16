# CRT Python Training - Day 12

# Date: 16 September 2026

# 1. Basic function without arguments

def addition():
    a, b = map(int, input('Enter two values: ').split())
    print(a + b)


# Function call
# addition()


# 2. Function with multiple statements

def subjects():
    print('Computer Networks')
    print('DBMS')
    print('Python')
    print('CSE')


# Function call
# subjects()


# 3. Function using pass

def f1():
    pass


# 4. Linear search using a function

def linear_search(list_v, ele):
    for i in list_v:
        if i == ele:
            return True
    return False


list_v = list(map(int, input('Enter n elements: ').split()))
ele = int(input('Enter element to be found: '))

if linear_search(list_v, ele):
    print('Element found in the list')
else:
    print('Element not found in the list')


# 5. Find the index of a given element

def index_search(list_v, ele):
    for i in range(len(list_v)):
        if list_v[i] == ele:
            return i
    return -1


a = [10, 20, 30, 40, 50, 60, 70]
ele = 40

index = index_search(a, ele)

if index != -1:
    print('Element found at', index)
else:
    print('Element not found')


# 6. Returning multiple values

def returnvalues():
    return 10, 'india', 10 + 4j


# Case 1 - Using multiple variables
t1, t2, t3 = returnvalues()
print(t1, t2, t3)


# Case 2 - Using a single variable
temp = returnvalues()
print(temp)


# Case 3 - Using unpacking
temp = returnvalues()
t1, t2, t3 = temp
print(t1, t2, t3)


# 7. Returning list elements

def display(arr):
    return arr


arr = [20, 30, 40, 50, 60]

print(display(arr))


# 8. Using returned list elements

temp = display(arr)

for x in temp:
    print(x, end=' ')

print()


# 9. Returning two different list values

def listvalues(arr1, arr2):
    return arr1, arr2


arr1 = [10, 20, 30, 40]
arr2 = [50, 60, 70, 80]

print(listvalues(arr1, arr2))


# 10. Storing returned lists in separate variables

temp1, temp2 = listvalues(arr1, arr2)

print(temp1, temp2)


# 11. Unpacking returned lists

print(*temp1, *temp2)


# 12. Nested function

def outer_fun():
    print('Hello')

    def inner_fun():
        print('I am in')

    inner_fun()


outer_fun()


# 13. Nested function with arguments

def outer_fun1():
    def inner_fun(p, q):
        return p + q

    temp = inner_fun(10, 20)
    print(temp)


outer_fun1()


# 14. Returning the inner function result

def outer():
    def inner():
        return 10 + 20

    return inner()


temp = outer()
print(temp)


# 15. Inner function returning multiple values

def outer_fun2():
    def inner_fun(a, b, c):
        return a, b, c

    return inner_fun(10, 20, 30)


t1, t2, t3 = outer_fun2()
print(t1, t2, t3)


# 16. Calling a function multiple times

def greet():
    print('Hello')


greet()
greet()
greet()
