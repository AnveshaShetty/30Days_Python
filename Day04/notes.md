# Day 04 - Strings

## 🎯 Topics Covered

- Creating Strings
- String Concatenation
- Escape Sequences
- String Formatting
- f-Strings
- String Indexing
- String Slicing
- String Methods
- String Membership
- String Length

---

## 📚 Concepts Learned

### Creating Strings

A string is a sequence of characters enclosed in:

- Single quotes `' '`
- Double quotes `" "`
- Triple quotes `''' '''` or `""" """` (for multi-line strings)

Example:

```python
first_name = "Anvesha"
country = "India"
```

---

### String Concatenation

Multiple strings can be combined using the `+` operator.

```python
full_name = first_name + " " + last_name
```

---

### Escape Sequences

Escape sequences allow special formatting inside strings.

| Escape Sequence | Description |
|----------------|-------------|
| `\n` | New line |
| `\t` | Tab space |
| `\\` | Backslash |
| `\'` | Single quote |
| `\"` | Double quote |

Example:

```python
print("Hello\nWorld")
```

---

### String Formatting

Python provides several ways to format strings.

#### Old Style

```python
"%s"
```

#### `format()` Method

```python
"Hello {}".format(name)
```

#### f-Strings (Recommended)

```python
print(f"My name is {name}")
```

f-Strings are the most readable and commonly used formatting method in modern Python.

---

### String Indexing

Each character in a string has an index.

Example:

```python
language = "Python"

language[0]   # P
language[-1]  # n
```

Python uses **zero-based indexing**.

---

### String Slicing

Extract a portion of a string.

```python
language[0:4]
language[2:]
language[::-1]
```

Used for:

- extracting text
- reversing strings
- skipping characters

---

### String Methods

Some commonly used string methods:

| Method | Purpose |
|---------|---------|
| `upper()` | Convert to uppercase |
| `lower()` | Convert to lowercase |
| `capitalize()` | Capitalize first letter |
| `title()` | Capitalize every word |
| `swapcase()` | Swap uppercase and lowercase |
| `strip()` | Remove leading/trailing spaces |
| `replace()` | Replace text |
| `split()` | Convert string to list |
| `join()` | Join list into string |
| `find()` | Find first occurrence |
| `rfind()` | Find last occurrence |
| `count()` | Count occurrences |
| `startswith()` | Check beginning of string |
| `endswith()` | Check ending of string |

---

### String Membership

Check whether a substring exists.

```python
"Python" in sentence
```

```python
"Java" not in sentence
```

---

### Useful Built-in Functions

```python
len()
```

Returns the number of characters in a string.

Example:

```python
len("Python")
```

---

## 📝 Key Takeaways

- Strings are immutable sequences of characters.
- Python uses zero-based indexing.
- Slicing allows extraction of specific portions of a string.
- f-Strings are the preferred way to format strings.
- String methods simplify text manipulation.
- Escape sequences improve output formatting.

---

## 🚀 Skills Practiced

- String Creation
- Concatenation
- Indexing
- Slicing
- String Formatting
- Escape Sequences
- Built-in Functions
- String Methods
- Membership Operators
- Text Manipulation

---

## 💡 Reflection

Today I learned how to work with Python strings effectively. I explored different ways to create, format, slice, and manipulate strings using built-in methods. Understanding string operations is essential because text processing is one of the most common tasks in Python programming.
