# Day 09 – CRT Python Training

# Tuples, Lists and Sets in Python

Today, I learned about three important collection-related data types in Python:

- Tuple
- List
- Set

These data types are used to store multiple values in a single variable.

---

## 1. Tuple

A tuple is one of the collection-related data types in Python.

- It is an in-built Python data structure.
- It allows us to store multiple values in a single variable.
- Different types of elements can be stored in a tuple.
- Tuple elements are ordered.
- Tuples are immutable.
- Tuples allow duplicate elements.
- Tuples use parentheses `()`.

### Creating an Empty Tuple

```python
t = ()
```

We can also create an empty tuple using:

```python
t = tuple()
```

### Tuple with a Single Element

A comma is required when creating a tuple with only one element.

```python
t = (10,)
```

Another way:

```python
t = 10,
```

### Tuple with Multiple Elements

```python
t = (10, 20, 30, 40, 50)
```

A tuple can contain different types of elements.

```python
t = (10, 20, 'Keerthi', 9.0 + 3j)
```

### Tuple Indexing

We can access tuple elements using indexes.

```python
t = (10, 20, 30)

print(t[0])
print(t[1])
print(t[2])
```

Indexing starts from `0`.

### Important Point

Tuple elements cannot be directly changed because tuples are immutable.

To modify tuple elements, we can convert the tuple into a list, make changes, and convert it back into a tuple.

---

## 2. List

A list is also an in-built Python collection-related data type.

- Lists can store multiple values.
- Different types of elements can be stored in a list.
- List elements are ordered.
- Lists are mutable.
- Lists allow duplicate elements.
- Lists use square brackets `[]`.

### Creating an Empty List

```python
l = []
```

Another way:

```python
l = list()
```

### Creating a List

```python
l = [10, 20, 30, 40, 50]
```

---

# List Methods

## append()

The `append()` method is used to add an element at the end of a list.

```python
l = [10, 20, 30]

l.append(40)

print(l)
```

Output:

```text
[10, 20, 30, 40]
```

---

## extend()

The `extend()` method is used to add multiple elements to a list.

```python
l = [10, 20, 30]

l.extend([40, 50, 60])

print(l)
```

---

## insert()

The `insert()` method is used to insert an element at a particular position.

Syntax:

```python
list.insert(index, element)
```

Example:

```python
l = [10, 20, 30]

l.insert(1, 15)

print(l)
```

---

## remove()

The `remove()` method is used to remove a specified element.

```python
l = [10, 20, 30, 40]

l.remove(20)

print(l)
```

---

## pop()

The `pop()` method is used to remove an element from a list.

```python
l = [10, 20, 30]

l.pop()

print(l)
```

---

## clear()

The `clear()` method is used to remove all elements from a list.

```python
l = [10, 20, 30]

l.clear()

print(l)
```

---

## index()

The `index()` method is used to find the position of an element.

```python
l = [10, 20, 30]

print(l.index(20))
```

---

## count()

The `count()` method is used to find how many times an element occurs.

```python
l = [10, 20, 10, 30, 10]

print(l.count(10))
```

---

# Accessing List Elements

List elements can be accessed using indexes.

```python
l = [1, 2, 3]

print(l[0])
print(l[1])
print(l[2])
```

---

# Nested Lists

A nested list is a list containing other lists.

```python
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

We can access nested elements using multiple indexes.

```python
print(my_list[0])
print(my_list[1])
print(my_list[2])

print(my_list[0][1])
```

---

## 3. Set

A set is also an in-built Python collection-related data type.

- Sets can store multiple values.
- Set elements are unordered.
- Sets do not allow duplicate elements.
- Sets are mutable.
- Set elements are unique.
- Indexing is not possible in sets.
- Sets use curly brackets `{}`.

### Creating an Empty Set

```python
s = set()
```

We should not use:

```python
s = {}
```

because `{}` creates an empty dictionary.

### Creating a Set

```python
s = {10, 20, 30}
```

---

# Set Methods

## add()

The `add()` method is used to add one element to a set.

```python
s = {10, 20, 30}

s.add(40)

print(s)
```

---

## update()

The `update()` method is used to add multiple elements to a set.

```python
s = {10, 20, 30}

s.update([40, 50])

print(s)
```

---

## remove()

The `remove()` method is used to remove a specified element.

```python
s = {10, 20, 30}

s.remove(20)

print(s)
```

---

## discard()

The `discard()` method is also used to remove an element from a set.

```python
s = {10, 20, 30}

s.discard(20)

print(s)
```

---

# Characteristics of Sets

- Set elements are unordered.
- Set elements are unique.
- Duplicate elements are not allowed.
- Indexing is not possible.

---

# Difference Between Tuple, List and Set

## Tuple

- Ordered
- Immutable
- Allows duplicate elements
- Supports indexing
- Uses `()`

## List

- Ordered
- Mutable
- Allows duplicate elements
- Supports indexing
- Uses `[]`

## Set

- Unordered
- Mutable
- Does not allow duplicate elements
- Does not support indexing
- Uses `{}`

---

# Key Takeaways

- Tuple, list and set are collection-related data types in Python.
- Tuples are ordered and immutable.
- Lists are ordered and mutable.
- Sets are unordered and contain unique elements.
- Lists and tuples allow duplicate values.
- Sets do not allow duplicate values.
- Lists and tuples support indexing.
- Sets do not support indexing.
- Different methods help us add, remove and update elements.

## Learn • Practice • Grow 🚀
