# Day 14 - Higher-Order Functions

## 🎯 Topics Covered

- Higher-Order Functions
- map()
- filter()
- reduce()
- Function Chaining
- Lambda Functions
- List Processing
- Working with Country Data
- Custom Functions
- Data Analysis

---

# 📚 Concepts Learned

## Higher-Order Functions

Higher-order functions are functions that either:

- Accept another function as an argument.
- Return another function.

Python provides several built-in higher-order functions such as:

- `map()`
- `filter()`
- `reduce()`

These functions simplify data processing and make code more concise.

---

## map()

The `map()` function applies a function to every element of an iterable and returns a map object.

General syntax:

```python
map(function, iterable)
```

Examples practiced:

- Convert country names to uppercase
- Convert names to uppercase
- Square every number

Example:

```python
numbers = [1,2,3]

squares = list(map(lambda x: x**2, numbers))
```

---

## filter()

The `filter()` function selects only those elements that satisfy a condition.

General syntax:

```python
filter(function, iterable)
```

Practiced filtering:

- Countries containing `"land"`
- Countries with exactly six letters
- Countries having six or more letters
- Countries starting with `"E"`

Example:

```python
filtered = list(filter(lambda country: "land" in country, countries))
```

---

## reduce()

The `reduce()` function repeatedly combines elements of an iterable into a single value.

It is available from:

```python
from functools import reduce
```

General syntax:

```python
reduce(function, iterable)
```

Practiced:

- Sum of numbers
- Concatenating country names into a sentence

Example:

```python
total = reduce(lambda x, y: x + y, numbers)
```

---

## Function Chaining

Combined multiple operations together.

Typical workflow:

```
Data
   ↓
Filter
   ↓
Map
   ↓
Reduce
```

Example:

```python
Even Numbers
      ↓
Square
      ↓
Sum
```

This technique improves readability and allows efficient data processing.

---

## String Filtering

Created a function that returns only string values from a mixed list.

Example:

```python
["hello", "world", "python"]
```

using:

```python
isinstance(item, str)
```

---

## Country Data Processing

Worked extensively with the countries dataset.

Implemented functions to:

- Return the first ten countries.
- Return the last ten countries.
- Filter countries containing specific patterns.
- Categorize countries.
- Count countries by starting letter.

These exercises demonstrated practical applications of loops, dictionaries, and higher-order functions.

---

## Dictionary Construction

Created a dictionary where:

- Keys → First letters
- Values → Number of countries beginning with that letter

Example:

```python
{
    "A": 11,
    "B": 17,
    ...
}
```

This introduced basic frequency counting.

---

## Reusable Functions

Created reusable helper functions such as:

- `get_first_ten_countries()`
- `get_last_ten_countries()`
- `categorize_countries()`
- `count_countries_by_letter()`
- `get_string_lists()`

These functions improve code organization and reusability.

---

# 📝 Key Takeaways

- Learned how higher-order functions simplify programming.
- Used `map()` to transform data.
- Used `filter()` to select data.
- Used `reduce()` to combine data.
- Chained multiple operations together.
- Built reusable functions.
- Worked with real-world datasets.
- Improved functional programming skills.

---

# 🛠️ Python Features Practiced

| Feature | Purpose |
|---------|---------|
| `map()` | Transform data |
| `filter()` | Select data |
| `reduce()` | Combine data |
| `lambda` | Anonymous functions |
| `isinstance()` | Type checking |
| `upper()` | Convert text to uppercase |
| `range()` | Generate sequences |
| Dictionaries | Frequency counting |
| Lists | Store processed data |
| Functions | Code reusability |

---

# 🚀 Skills Practiced

- Higher-Order Functions
- Functional Programming
- map()
- filter()
- reduce()
- Lambda Functions
- Data Filtering
- Data Transformation
- Dictionaries
- Problem Solving

---

# 💡 Reflection

Today I explored Python's higher-order functions and learned how they simplify data processing. I practiced transforming data using `map()`, filtering data using `filter()`, and combining values using `reduce()`. I also worked with a real-world dataset of countries to build reusable functions for filtering, categorizing, and analyzing data. These concepts introduced me to functional programming techniques that make Python code more concise, readable, and efficient.
