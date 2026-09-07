# Day 06 – Control Statements in Python

Date:7 September 2026

## Control Statements

Control statements are used to control the flow of execution of a program based on certain conditions.

To control the flow of execution of any program in Python, we require expressions such as:

- Relational operators
- Logical operators
- Membership operators
- Other conditional expressions

Control statements are divided into three different parts:

1. Selection Statements
2. Looping Statements
3. Jumping / Transfer Statements

---

## 1. Selection Statements

Selection statements are also called decision-making statements.

They are used to execute a block of statements based on a condition.

### Types of Selection Statements

- Simple if
- if-else
- elif
- Nested if
- Multiple if
- match-case

---

### Simple if Statement

The if statement is used for comparison and executes a block of statements when the condition is true.

#### Syntax

    if condition:
        statement

#### Important Points

- The result may be True or False.
- If the condition is True, the block statement is executed.
- If the condition is False, the block statement is not executed.
- Indentation is very important in Python.

---

### if-else Statement

The if-else statement provides two possible paths of execution.

If the condition is true, the if block is executed.

Otherwise, the else block is executed.

#### Syntax

    if condition:
        statement
    else:
        statement

---

### elif Statement

The elif statement is used to check multiple conditions.

If one condition is false, the next condition can be checked.

#### Syntax

    if condition_1:
        statement
    elif condition_2:
        statement
    else:
        statement

---

### Nested if Statement

A nested if statement means an if statement inside another if statement.

#### Syntax

    if condition_1:
        if condition_2:
            statement

---

### Multiple if Statements

Multiple if statements are used when multiple conditions need to be checked independently.

#### Syntax

    if condition_1:
        statement

    if condition_2:
        statement

    if condition_3:
        statement

---

## 2. Looping Statements

Looping statements are also called iterative statements.

They are used to execute statements repeatedly.

### for Loop

A for loop is used to execute statements a limited number of times.

### while Loop

A while loop is used to execute statements repeatedly based on a condition until the condition becomes false.

---

## 3. Jumping / Transfer Statements

Jumping or transfer statements are used to change the normal flow of execution.

The jumping statements are:

- break
- continue
- pass
- return

---

## match-case

The match-case statement is used to compare one value with multiple values or cases.

It is used for selecting one option from a list of options.

### Examples

- Searching IVR options
- Customer care systems

The match-case statement is equivalent to the switch-case concept in other programming languages like C and Java.

It was introduced in Python version 3.10.

### Syntax

    match value:
        case 1:
            statement

        case 2:
            statement

        case 3:
            statement

        case _:
            statement

### Note

There is no need to use break in Python match-case.
