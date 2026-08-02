# Day 13 - List Comprehension & Lambda Functions

## 🎯 Topics Covered

- List Comprehension
- Conditional List Comprehension
- Nested List Comprehension
- Flattening Lists
- Creating Lists of Tuples
- Creating Lists of Dictionaries
- String Concatenation
- Lambda Functions
- Data Transformation

---

# 📚 Concepts Learned

## List Comprehension

List comprehension provides a concise and readable way to create new lists.

General syntax:

```python
new_list = [expression for item in iterable]
```

Example:

```python
squares = [x ** 2 for x in range(6)]
```

It helps replace traditional loops with a shorter and more Pythonic approach.

---

## Conditional List Comprehension

Conditions can be added to filter elements.

Example:

```python
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

non_positive = [num for num in numbers if num <= 0]
```

This creates a new list containing only the required elements.

---

## Flattening Nested Lists

Used nested list comprehension to convert multi-dimensional lists into a single list.

Example:

```python
list_of_lists = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

flattened = [
    number
    for row in list_of_lists
    for number in row
]
```

Result:

```python
[1,2,3,4,5,6,7,8,9]
```

---

## Creating Lists of Tuples

Generated tuples containing multiple mathematical values.

Example:

```python
(i, 1, i, i², i³, i⁴, i⁵)
```

using list comprehension and `range()`.

---

## Working with Nested Data

Converted nested country data into structured lists.

Example output:

```python
[
    ['FINLAND', 'FIN', 'HELSINKI'],
    ['SWEDEN', 'SWE', 'STOCKHOLM']
]
```

This demonstrated how list comprehension can transform complex data structures.

---

## List of Dictionaries

Created dictionaries directly using list comprehension.

Example:

```python
{
    "country": "FINLAND",
    "city": "HELSINKI"
}
```

This is a common technique in data processing and API development.

---

## String Concatenation

Combined first and last names into a single string.

Example:

```python
"Asabeneh Yetayeh"
```

using formatted strings inside list comprehension.

---

## Lambda Functions

Lambda functions are small anonymous functions written in a single line.

General syntax:

```python
lambda parameters: expression
```

Examples:

```python
square = lambda x: x ** 2
```

Practiced using lambda functions to calculate:

- Slope
- y-intercept

of a straight line.

---

## Data Transformation

One of the biggest lessons today was learning how Python can transform data using only a single line of code.

Examples included:

- Filtering
- Mapping
- Flattening
- Formatting
- Creating new structures

---

# 📝 Key Takeaways

- Learned how list comprehension replaces many traditional loops.
- Used conditions inside list comprehensions.
- Flattened nested lists efficiently.
- Created tuples and dictionaries dynamically.
- Transformed nested datasets into structured output.
- Learned the syntax and use cases of lambda functions.
- Improved code readability while reducing the number of lines.

---

# 🛠️ Python Features Practiced

| Feature | Purpose |
|---------|---------|
| List Comprehension | Create lists efficiently |
| Conditional Expressions | Filter data |
| Nested Loops | Flatten nested structures |
| Lambda Functions | Anonymous functions |
| f-Strings | Format strings |
| Dictionaries | Store structured data |
| Tuples | Store immutable values |
| `range()` | Generate sequences |
| `upper()` | Convert text to uppercase |

---

# 🚀 Skills Practiced

- List Comprehension
- Nested List Comprehension
- Conditional Filtering
- Data Transformation
- Lambda Functions
- Nested Data Structures
- Dictionaries
- Tuples
- String Formatting
- Problem Solving

---

# 💡 Reflection

Today I learned one of Python's most powerful and expressive features—**list comprehension**. I practiced creating, filtering, and transforming data using concise syntax, making my code cleaner and easier to read. I also explored **lambda functions**, which helped me understand how simple functions can be written in a single line. These concepts are widely used in data analysis, automation, and software development, making them valuable additions to my Python toolkit.
