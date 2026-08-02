# Day 18 - Regular Expressions (Regex)
---

# 🎯 Topics Covered

- Introduction to Regular Expressions (Regex)
- `re` Module
- Pattern Matching
- Special Characters
- Character Classes
- Quantifiers
- `findall()`
- `search()`
- `match()`
- `sub()`
- Validating Python Variables
- Extracting Numbers from Text
- Word Frequency Analysis

---

# 📚 Introduction

Regular Expressions (Regex) are patterns used to search, match, extract, and manipulate text.

Python provides the built-in **`re`** module to work with regular expressions.

Regex is widely used in:

- Input validation
- Email verification
- Password validation
- Data extraction
- Search engines
- Web scraping
- Log analysis

---

# 📦 Importing Regex

```python
import re
```

---

# 1. Finding Patterns

The most commonly used function is:

```python
re.findall(pattern, text)
```

It returns **all matches** found in a string.

Example

```python
import re

text = "Python is fun"

result = re.findall(r"Python", text)

print(result)
```

Output

```
['Python']
```

---

# 2. Character Classes

| Pattern | Meaning |
|----------|---------|
| `\d` | Digit (0-9) |
| `\D` | Not a digit |
| `\w` | Letter, digit or underscore |
| `\W` | Not a word character |
| `\s` | Whitespace |
| `\S` | Non-whitespace |

Example

```python
re.findall(r"\d", "Age: 20")
```

Output

```
['2', '0']
```

---

# 3. Quantifiers

| Symbol | Meaning |
|----------|---------|
| `*` | 0 or more |
| `+` | 1 or more |
| `?` | Optional |
| `{n}` | Exactly n |
| `{m,n}` | Between m and n |

Example

```python
re.findall(r"\d+", "Age 20 Roll 105")
```

Output

```
['20', '105']
```

---

# 4. Common Regex Functions

### `findall()`

Returns every match.

```python
re.findall(pattern, text)
```

---

### `search()`

Returns the first occurrence.

```python
re.search(pattern, text)
```

---

### `match()`

Checks only from the beginning.

```python
re.match(pattern, text)
```

---

### `sub()`

Replaces text.

```python
re.sub(pattern, replacement, text)
```

Example

```python
re.sub("Python", "Java", "Python Programming")
```

Output

```
Java Programming
```

---

# 5. Finding the Most Frequent Words

Main steps:

- Convert text to lowercase
- Extract words using Regex
- Count word occurrences
- Sort by frequency

```python
re.findall(r'\b\w+\b', paragraph.lower())
Counter(words)
```

---

# 6. Extracting Numbers from Text

Regex can extract numbers from long sentences.

Example

```python
numbers = re.findall(r'-?\d+', text)
```

Pattern explanation:

- `-?` → optional negative sign
- `\d+` → one or more digits
---

# 7. Validating Python Variable Names

A valid Python variable:

✅ Can start with:

- Letter
- Underscore

❌ Cannot start with:

- Number

Regex pattern:

```python
^[a-zA-Z_][a-zA-Z0-9_]*$
```

Meaning:

- `^` → start of string
- `[a-zA-Z_]` → first character must be a letter or underscore
- `[a-zA-Z0-9_]*` → remaining characters can be letters, digits, or underscores
- `$` → end of string
- 
---

# 📌 Useful Regex Symbols

| Symbol | Meaning |
|----------|---------|
| `.` | Any character |
| `^` | Beginning of string |
| `$` | End of string |
| `[]` | Character class |
| `()` | Group |
| `|` | OR |
| `+` | One or more |
| `*` | Zero or more |
| `?` | Optional |
| `{}` | Number of repetitions |

---

# 📖 Examples

### Find all numbers

```python
re.findall(r"\d+", text)
```

---

### Find words

```python
re.findall(r"\w+", text)
```

---

### Remove spaces

```python
re.sub(r"\s+", "", text)
```

---

### Replace digits

```python
re.sub(r"\d", "*", text)
```

---

# ⚠️ Common Mistakes

### Forgetting the raw string (`r`)

Wrong

```python
"\d+"
```

Correct

```python
r"\d+"
```

---

### Using `match()` instead of `search()`

`match()` checks **only the beginning** of the string.

Use `search()` if the pattern can appear anywhere.

---

# 📝 Key Takeaways

- Regex is used for searching and manipulating text.
- Python uses the `re` module for regular expressions.
- `findall()` returns every matching pattern.
- `search()` returns the first match.
- `match()` checks only from the beginning of the string.
- `sub()` replaces matched text.
- Regex can validate variable names, extract numbers, and process text efficiently.

---

# 🚀 Skills Practiced

- Importing the `re` module
- Finding text patterns
- Using character classes and quantifiers
- Extracting numbers from text
- Counting word frequencies
- Validating Python variable names
- Working with `Counter` and Regex together

---

# 💡 Reflection

Today I explored the power of Regular Expressions (Regex) in Python. I learned how to search for patterns, extract numbers from text, count the frequency of words, and validate Python variable names using regular expressions. I also practiced using the `re` module alongside the `Counter` class to solve text-processing problems more efficiently. Regex is an essential skill for data validation, web scraping, log analysis, and real-world text processing.
