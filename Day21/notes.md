# Day 21 - Python Classes (Statistics Project)

# 🎯 Topics Covered

- Python Classes
- Constructors (`__init__`)
- Instance Variables
- Creating Objects
- Class Methods
- Using Python's `statistics` Module
- `collections.Counter`
- Building a Statistics Calculator
- Frequency Distribution
- Object-Oriented Programming (OOP)

---

# 📚 Introduction

Today's challenge focused on **Object-Oriented Programming (OOP)** by creating a custom `Statistics` class.

Instead of writing separate functions, all statistical operations were grouped inside a single class. The program calculates:

- Count
- Sum
- Minimum
- Maximum
- Range
- Mean
- Median
- Mode
- Variance
- Standard Deviation
- Frequency Distribution

using built-in Python modules and custom methods. 

---

# 1. What is a Class?

A **class** is a blueprint used to create objects.

It groups:

- Variables (attributes)
- Functions (methods)

inside one reusable structure.

Syntax

```python
class ClassName:
    pass
```

---

# 2. Constructor (`__init__`)

A constructor runs automatically whenever an object is created.

Syntax

```python
class Student:

    def __init__(self, name):
        self.name = name
```

In this project:

```python
class Statistics:

    def __init__(self, data):
        self.data = sorted(data)
```

The constructor stores the dataset after sorting it. 

---

# 3. Creating an Object

Objects are created from classes.

Example

```python
ages = [...]

data = Statistics(ages)
```

Now every statistical function can be accessed through `data`. 

---

# 4. Instance Variable

Variables beginning with

```python
self.
```

belong to each object.

Example

```python
self.data
```

stores the list of ages.

---

# 5. Methods Created

The project contains the following methods:

### count()

Returns total number of values.

```python
data.count()
```

---

### sum()

Returns total sum.

```python
data.sum()
```

---

### min()

Returns smallest value.

```python
data.min()
```

---

### max()

Returns largest value.

```python
data.max()
```

---

### range()

Formula

```
Maximum − Minimum
```

---

### mean()

Uses

```python
statistics.mean()
```

Returns average value.

---

### median()

Uses

```python
statistics.median()
```

Returns middle value.

---

### mode()

Uses

```python
statistics.mode()
```

Returns

```
(mode, frequency)
```

Example

```
(26,5)
```

meaning

```
26 appears five times.
```

---

### std()

Calculates Standard Deviation.

Uses

```python
statistics.stdev()
```

---

### var()

Calculates Variance.

Uses

```python
statistics.variance()
```

---

### freq_dist()

Creates Frequency Distribution.

Uses

```python
Counter()
```

from

```python
collections
```

The values are sorted by highest frequency and returned as percentage-value pairs.

---

### describe()

Returns all statistical information together as formatted text by combining the outputs of every method. 

---

# 6. Modules Used

### statistics

Imported functions:

```python
from statistics import

mean
median
mode
stdev
variance
```

These perform common statistical calculations.

---

### collections.Counter

```python
from collections import Counter
```

Used to count how many times each number appears in the dataset.

Example

```
26 → 5

27 → 4

32 → 3
```

---

# 7. Frequency Distribution

The project converts frequencies into percentages.

Formula

```
(count / total) × 100
```

Example Output

```
[(20.0,26),
 (16.0,27),
 (12.0,32),
 ...]
```

Meaning

```
26 appears in 20% of the data.
```

---

# 8. Sample Dataset

```python
ages = [
31,26,34,37,27,
26,32,32,26,27,
27,24,32,33,27,
25,26,38,37,31,
34,24,33,29,26
]
```

---

# 9. Output

```
Count : 25

Sum : 744

Minimum : 24

Maximum : 38

Range : 14

Mean : 30

Median : 29

Mode : (26,5)

Variance : 18.3

Standard Deviation : 4.3

Frequency Distribution :

[(20.0,26),
(16.0,27),
(12.0,32),
...]
```

These values are produced by creating a `Statistics` object and calling its methods. 

---

# 📌 Important Concepts

| Concept | Description |
|----------|-------------|
| Class | Blueprint for objects |
| Object | Instance of a class |
| Constructor | `__init__()` initializes objects |
| self | Refers to the current object |
| Method | Function inside a class |
| Instance Variable | Variable belonging to an object |
| Counter | Counts occurrences of elements |
| statistics | Built-in module for statistical calculations |

---

# 📖 Examples

### Creating a class

```python
class Statistics:
```

---

### Constructor

```python
def __init__(self,data):
    self.data=data
```

---

### Creating an object

```python
data = Statistics(ages)
```

---

### Calling methods

```python
data.mean()

data.median()

data.std()
```

---

### Counting frequency

```python
Counter(self.data)
```

---

### Using statistics module

```python
mean(data)

median(data)

mode(data)

stdev(data)

variance(data)
```

---

# ⚠️ Common Mistakes

### Forgetting `self`

Wrong

```python
def mean():
```

Correct

```python
def mean(self):
```

---

### Forgetting object name

Wrong

```python
mean()
```

Correct

```python
data.mean()
```

---

### Empty dataset

Creating the class with an empty list raises:

```python
ValueError
```

because the constructor checks whether the data list is empty before continuing. 

---

### Forgetting parentheses

Wrong

```python
data.mean
```

Correct

```python
data.mean()
```

---

# 📝 Key Takeaways

- Classes group related data and methods together.
- Objects are instances of classes.
- Constructors initialize object data.
- `self` represents the current object.
- Python's `statistics` module simplifies statistical calculations.
- `Counter` efficiently counts occurrences.
- A single class can provide multiple related operations through methods.
- The `describe()` method offers a clean summary of all calculated statistics.

---

# 🚀 Skills Practiced

- Creating classes
- Using constructors
- Working with objects
- Writing class methods
- Using instance variables
- Importing built-in modules
- Applying the `statistics` module
- Using `collections.Counter`
- Calculating statistical measures
- Building a reusable statistics calculator

---

# 💡 Reflection

Today I learned the fundamentals of Object-Oriented Programming by designing a `Statistics` class that organizes multiple statistical operations into reusable methods. I practiced creating classes, constructors, objects, and instance variables while also using Python's built-in `statistics` module and `collections.Counter` to calculate descriptive statistics and frequency distributions. This project demonstrated how OOP makes code cleaner, reusable, and easier to maintain.
