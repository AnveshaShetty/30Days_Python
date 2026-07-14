# Day 05 - Lists

## 🎯 Topics Covered

- Creating Lists
- Accessing List Elements
- List Unpacking
- Nested Data Types
- List Methods
- Membership Operators
- List Slicing
- List Sorting
- List Reversal
- Copying Lists
- Joining Lists
- List Deletion
- Working with Real-world Data
- Basic Statistical Calculations

---

## 📚 Concepts Learned

### Creating Lists

Lists are ordered, mutable collections that can store multiple values of different data types.

Examples:

```python
movies = ['Scream', 'It', 'Mama']

empty = []
```

---

### Mixed Data Types

A single list can contain different data types.

```python
mixed_data = [
    'Anvesha',
    20,
    {'height': '5.3ft'},
    {'country': 'India'}
]
```

---

### List Unpacking

Used unpacking to extract the first, middle, and last elements.

```python
first, *middle, last = movies
```

This makes accessing multiple elements much easier.

---

### Accessing & Modifying Lists

Accessed elements using indexing.

```python
it_companies[0]
```

Modified list elements.

```python
it_companies[0] = "Nvidia"
```

---

### Adding Elements

Learned different ways to add data.

```python
append()
insert()
extend()
```

Examples:

```python
it_companies.append("TCS")
it_companies.insert(4, "Infosys")
front_end.extend(back_end)
```

---

### Joining Strings

Converted list elements into a single string.

```python
"#; ".join(it_companies)
```

---

### Membership Operators

Checked whether an item exists inside a list.

```python
"IBM" in it_companies
```

---

### Sorting Lists

Sorted data alphabetically.

```python
sort()
```

Reversed the list.

```python
reverse()
```

---

### List Slicing

Extracted portions of a list.

Examples:

```python
list[:3]
list[-3:]
list[4:5]
```

---

### Removing Elements

Practiced multiple deletion methods.

```python
del
pop()
clear()
```

Also learned the difference between:

- Removing elements
- Clearing a list
- Deleting the entire list

---

### Working with Large Lists

Worked with a list containing nearly 200 countries.

Practiced:

- Finding middle element(s)
- Dividing the list into two halves
- Unpacking selected countries

---

### Copying Lists

Created an independent copy of a list.

```python
copy()
```

---

### Combining Lists

Merged frontend and backend technologies.

```python
extend()
```

Created a Full Stack technology list.

---

### Statistical Calculations

Used a list of ages to calculate:

- Minimum value
- Maximum value
- Average
- Median
- Range

Built-in functions used:

```python
min()
max()
sum()
len()
```

---

## 📝 Key Takeaways

- Lists are mutable, allowing elements to be modified.
- Learned how to create, access, update and delete list elements.
- Practiced list unpacking using the `*` operator.
- Used common list methods like `append()`, `insert()`, `extend()`, `sort()`, `reverse()`, `copy()`, and `clear()`.
- Worked with real-world datasets such as country names and company names.
- Applied list operations to solve practical programming problems.
- Performed basic statistical analysis using Python's built-in functions.

---

## 🛠️ List Methods Practiced

| Method | Purpose |
|---------|---------|
| `append()` | Add an item at the end |
| `insert()` | Insert an item at a specific index |
| `extend()` | Combine two lists |
| `copy()` | Create a copy of a list |
| `sort()` | Sort elements |
| `reverse()` | Reverse the list |
| `pop()` | Remove an element by index |
| `clear()` | Remove all elements |

---

## 🚀 Skills Practiced

- Lists
- Indexing
- Slicing
- Unpacking
- Nested Lists
- List Methods
- Membership Operators
- Sorting Algorithms
- Data Manipulation
- Statistical Calculations
- Built-in Functions
- Problem Solving

---

## 💡 Reflection

Today I explored one of Python's most powerful data structures—**lists**. I learned how to create, modify, sort, slice, combine, and analyze lists using built-in methods and functions. Through practical exercises involving IT companies, countries, technologies, and age statistics, I strengthened my understanding of data manipulation and improved my problem-solving skills. Lists are fundamental to Python programming, and today's practice gave me a solid foundation for working with collections of data.
