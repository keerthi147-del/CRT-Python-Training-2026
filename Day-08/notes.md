# 🐍 CRT Python Training – Day 08

## Topic: Python Lists and List Operations

# What is a List?

A list is a predefined or built-in data structure in Python used to store multiple elements in a single variable.

### Example

    list_variable = [10, 40, 890]

### Important Points

- A list can store multiple elements in a single variable.
- Lists are represented using square brackets `[]`.
- Elements are separated by commas.
- Lists are mutable.
- Lists can contain duplicate elements.
- Lists can store different data types.

### Example

    values = [10, 'Keerthi', 20.5, True]

---

# 📌 Creating a List

## Method 1: Using Square Brackets

    list1 = [10, 20, 30]

## Method 2: Using the list() Function

    list1 = list((10, 20, 30))

---

# 📌 Accessing List Elements

List elements can be accessed using their index values.

### Example

    list1 = [10, 20, 30, 40, 50]

    print(list1[0])

### Output

    10

---

# 📌 Positive Indexing

Positive indexing starts from `0`.

    Index:    0   1   2   3   4
    List:    10  20  30  40  50

### Example

    list1 = [10, 20, 30, 40, 50]

    print(list1[0])
    print(list1[2])

---

# 📌 Negative Indexing

Negative indexing starts from `-1`.

    Index:   -5  -4  -3  -2  -1
    List:    10  20  30  40  50

### Example

    list1 = [10, 20, 30, 40, 50]

    print(list1[-1])

### Output

    50

---

# 📌 Accessing Elements Using Indexing

    list1 = [10, 20, 30, 40, 50]

    print(list1[0])
    print(list1[1])
    print(list1[2])

---

# 📌 List Slicing

Slicing is used to access multiple elements from a list.

## Syntax

    list[start:end]

The end index is not included.

### Example

    list1 = [10, 20, 30, 40, 50]

    print(list1[1:4])

### Output

    [20, 30, 40]

---

# 📌 Slicing with Step Value

## Syntax

    list[start:end:step]

### Example

    list1 = [10, 20, 30, 40, 50, 60]

    print(list1[1:6:2])

---

# 📌 List Methods

Python provides different methods to perform operations on lists.

Important methods include:

- `append()`
- `extend()`
- `insert()`
- `remove()`
- `pop()`
- `clear()`

---

# ➕ append()

The `append()` method is used to add one element at the end of a list.

## Syntax

    list.append(element)

### Example

    list1 = []

    list1.append(10)

    print(list1)

### Output

    [10]

---

# ➕ Adding Multiple Elements Using append()

    list1 = []

    list1.append(10)
    list1.append(20)
    list1.append(30)

    print(list1)

### Output

    [10, 20, 30]

---

# ➕ extend()

The `extend()` method is used to add multiple elements to an existing list.

## Syntax

    list.extend(elements)

### Example

    list1 = []

    list1.extend([10, 20, 30])

    print(list1)

### Output

    [10, 20, 30]

---

# 📌 Difference Between append() and extend()

## append()

`append()` adds the given value as a single element.

### Example

    list1 = []

    list1.append([10, 20, 30])

    print(list1)

### Output

    [[10, 20, 30]]

## extend()

`extend()` adds individual elements to the list.

### Example

    list1 = []

    list1.extend([10, 20, 30])

    print(list1)

### Output

    [10, 20, 30]

---

# ➕ insert()

The `insert()` method is used to add an element at a particular index position.

## Syntax

    list.insert(index, element)

### Example

    list1 = [10, 20, 30]

    list1.insert(1, 15)

    print(list1)

### Output

    [10, 15, 20, 30]

---

# ❌ remove()

The `remove()` method is used to remove a specified element from a list.

## Syntax

    list.remove(element)

### Example

    list1 = [10, 20, 30, 20]

    list1.remove(20)

    print(list1)

### Output

    [10, 30, 20]

`remove()` removes the first matching element.

---

# ❌ pop()

The `pop()` method is used to remove an element from a list.

### Example

    list1 = [10, 20, 30]

    list1.pop()

    print(list1)

### Output

    [10, 20]

By default, `pop()` removes the last element.

We can also remove an element using its index.

### Example

    list1 = [10, 20, 30]

    list1.pop(1)

    print(list1)

### Output

    [10, 30]

---

# ❌ del Keyword

The `del` keyword is used to delete elements from a list.

### Example

    list1 = [10, 20, 30]

    del list1[1]

    print(list1)

### Output

    [10, 30]

---

# ❌ clear()

The `clear()` method removes all elements from a list.

### Example

    list1 = [10, 20, 30]

    list1.clear()

    print(list1)

### Output

    []

---

# 📌 Nested List

A nested list is a list containing another list as an element.

### Example

    list1 = [10, 20, [30, 40], 50]

    print(list1)

---

# 📌 Accessing Elements in a Nested List

### Example

    list1 = [10, 20, [30, 40], 50]

    print(list1[2])

### Output

    [30, 40]

To access an individual element inside the nested list:

    print(list1[2][0])

### Output

    30

---

# 📌 List is Mutable

Lists are mutable, which means we can modify their elements.

### Example

    list1 = [10, 20, 30]

    list1[1] = 25

    print(list1)

### Output

    [10, 25, 30]

---

# 📌 List Summary

- Lists are represented using `[]`.
- Lists can store multiple elements.
- Lists are mutable.
- Lists allow duplicate values.
- Lists can contain different data types.
- List elements can be accessed using indexing.
- Positive and negative indexing can be used.
- Slicing can be used to access multiple elements.
- Elements can be added using `append()`, `extend()` and `insert()`.
- Elements can be removed using `remove()`, `pop()`, `del` and `clear()`.
- Lists can contain nested lists.

---

## 🌱 Key Takeaway

Python lists are flexible and mutable data structures that allow us to store, access, modify, add and remove multiple values efficiently.
