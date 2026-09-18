
### Day-14/programs.py


# CRT Python Training - Day 14
# Topic: Object-Oriented Programming (OOP)

# 1. Creating a simple class
class A:
    pass


# 2. Creating an object of a class
obj = A()
print(obj)


# 3. Class with a method
class Demo:
    def display(self):
        print('Hello from Demo class')


obj = Demo()
obj.display()


# 4. Class with instance variables
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('Name:', self.name)
        print('Age:', self.age)


s1 = Student('Keerthi', 20)
s1.display()


# 5. Employee class using constructor
class EmpDetails:
    def __init__(self, name, id, salary, doj):
        self.name = name
        self.id = id
        self.salary = salary
        self.doj = doj

    def detail(self):
        print(f'Name of employee: {self.name}')
        print(f'Employee ID: {self.id}')
        print(f'Employee salary: {self.salary}')
        print(f'Date of join: {self.doj}')


# 6. Creating employee objects
y0 = EmpDetails('Deekshitha', 12, 100000, '12-05-27')
y1 = EmpDetails('Keerthi', 15, 100000, '15-09-27')
y2 = EmpDetails('Rithika', 4, 100000, '14-04-27')
y3 = EmpDetails('Rahul', 8, 90000, '10-06-27')


# 7. Calling the detail() method for each object
y0.detail()
y1.detail()
y2.detail()
y3.detail()
