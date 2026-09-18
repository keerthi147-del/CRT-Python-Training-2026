# CRT Python Training - Day 14

## Object-Oriented Programming (OOP)

### OOP - Object-Oriented Programming

Object-Oriented Programming is a programming concept commonly used in many programming languages like C++, Java and Python.

Python supports Object-Oriented Programming.

The main concepts discussed are:
- Class
- Object
- Properties
- Methods
- Constructor
- Reference variable

### Class

- A class is a user-defined data type.
- A class can contain properties and methods.
- Properties represent the data related to an object.
- Methods represent the operations performed by an object.
- A class is used as a blueprint for creating objects.
- A program can contain any number of classes.

Example:

    class Student:
        pass

### Object

- An object is an instance of a class.
- Objects are created from a class.
- A class can be used to create multiple objects.
- Objects can access the properties and methods of a class.

Example:

    class Student:
        pass

    s1 = Student()
    s2 = Student()

Here, s1 and s2 are objects of the Student class.

### Properties

- Properties represent the data or characteristics of an object.
- Properties are also called instance variables when they belong to a particular object.

Examples:
- Employee name
- Employee ID
- Employee salary
- Date of joining

### Methods

- A method is a function defined inside a class.
- Methods are used to perform operations related to an object.
- A method can be called using the object/reference variable.

Example:

    class Student:
        def display(self):
            print('Student details')

    s1 = Student()
    s1.display()

### Constructor

- A constructor is used to initialize the properties of an object.
- In Python, __init__() is used as the constructor.
- The __init__() method is automatically called when an object is created.
- It is used to initialize the values of an object.

Syntax:

    class ClassName:
        def __init__(self, arguments):
            statements

### self

- self represents the current object.
- It is used to access the properties and methods of the current object.
- self is generally written as the first parameter in instance methods.
- Different objects can have different values for their properties.

Example:

    class Student:
        def __init__(self, name):
            self.name = name

Here, self.name represents the name property of the current object.

### Reference Variable

- A reference variable refers to an object.
- Reference variables are used to access the properties and methods of an object.
- An object can be accessed using its reference variable.

Example:

    class Student:
        def display(self):
            print('Student details')

    s1 = Student()
    s1.display()

Here, s1 is the reference variable used to access the object.

### Calling a Method

A method can be called using the reference variable/object.

Example:

    class Student:
        def display(self):
            print('Student details')

    s1 = Student()
    s1.display()

Here, display() is called using the reference variable s1.

### Example - Employee Details

Write a Python program to initialize employee name, employee ID, employee salary and date of joining and print the details of different employees.

Program:

    class EmpDetails:

        def __init__(self, name, id, salary, doj):
            self.name = name
            self.id = id
            self.salary = salary
            self.doj = doj

        def details(self):
            print(f'Name of employee: {self.name}')
            print(f'ID: {self.id}')
            print(f'Salary: {self.salary}')
            print(f'Date of join: {self.doj}')


    y0 = EmpDetails('Deekshith', 12, 10000, '12-05-27')
    y1 = EmpDetails('Keerthi', 15, 100000, '16-09-27')
    y2 = EmpDetails('Rithu', 4, 10000, '14-04-27')

    y0.details()
    y1.details()
    y2.details()

### Important Points

- A class is a user-defined data type.
- An object is an instance of a class.
- A class can contain properties and methods.
- __init__() is used as the constructor.
- The constructor initializes object properties.
- self represents the current object.
- Reference variables are used to access objects.
- Methods are functions defined inside a class.
- A class can be used to create multiple objects.
- Each object can have its own property values.
- Methods can be called using the object/reference variable.

### Key Takeaways

- OOP organizes programs using classes and objects.
- A class acts as a blueprint for creating objects.
- Objects are instances of a class.
- Properties store object-related data.
- Methods perform operations related to objects.
- __init__() is used to initialize object properties.
- self refers to the current object.
- Reference variables are used to access objects and methods.
- Multiple objects can be created from the same class.
- Each object can have different property values.
