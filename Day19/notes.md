# Day 19 - File Handling & JSON Processing in Python

# 🎯 Topics Covered

- File Handling
- Reading Text Files
- Counting Lines and Words
- Working with JSON Files
- `json` Module
- `os` Module
- Error Handling (`try-except`)
- Sorting Data
- `collections.Counter`
- Processing Country Dataset
- Speech Text Analysis

---

# 📚 Introduction

Many real-world applications read information from files instead of asking the user to enter everything manually.

Python provides built-in functions to work with:

- Text files (`.txt`)
- JSON files (`.json`)
- CSV files
- Binary files

Today focused mainly on reading **text files** and **JSON data**, analyzing their contents, and extracting useful information.

---

# 1. Reading Text Files

Python uses the `open()` function to access files.

Syntax

```python
with open(filename, "r", encoding="utf-8") as file:
    data = file.read()
```

### Parameters

| Parameter | Meaning |
|-----------|---------|
| `"r"` | Read mode |
| `"w"` | Write mode |
| `"a"` | Append mode |
| `"utf-8"` | Character encoding |

Using `with` automatically closes the file after use.

---

# 2. Counting Lines and Words

A common file-processing task is counting:

- Number of lines
- Number of words

General approach:

```python
line_count = 0
word_count = 0

for line in file:
    line_count += 1
    word_count += len(line.split())
```

# 3. Working with Multiple Files

Instead of writing the same code repeatedly, store filenames inside a list.

Example

```python
speech_files = [
    "obama_speech.txt",
    "donald_speech.txt"
]
```

Loop through each file:

```python
for file_name in speech_files:
    count_lines_and_words(file_name)
```

This makes programs reusable and cleaner. 

---

# 4. JSON Files

JSON stands for:

> **JavaScript Object Notation**

It stores structured data using:

- Dictionaries
- Lists
- Strings
- Numbers
- Booleans

Example

```json
{
    "name": "India",
    "capital": "New Delhi",
    "population": 1400000000
}
```

The `countries_data.json` file contains country information such as the country's name, capital, languages, population, flag URL, and currency.

---

# 5. Loading JSON Data

Import the JSON module:

```python
import json
```

Load data:

```python
with open(filename, "r", encoding="utf-8") as file:
    countries = json.load(file)
```

`json.load()` converts JSON into Python objects.

---

# 6. Using the os Module

The `os` module helps work with file paths.

Example

```python
import os

os.path.exists(filename)
```

# 7. Finding the Most Spoken Languages

Steps:

1. Read the JSON file
2. Extract every country's language list
3. Combine all languages
4. Count each language
5. Return the top 10

You used:

```python
Counter(all_languages)
```

and

```python
most_common(top_n)
```

to determine the most frequently spoken languages across the dataset.

---

# 8. Finding the Most Populated Countries

Steps:

- Read JSON data
- Sort countries by population
- Return the top 10

Sorting:

```python
sorted(
    countries,
    key=lambda x: x["population"],
    reverse=True
)
```

# 9. collections.Counter

`Counter` counts repeated items automatically.

Example

```python
from collections import Counter

Counter(["A", "B", "A"])
```

Output

```
Counter({'A':2,'B':1})
```

Useful for:

- Word frequency
- Language frequency
- Character frequency

---

# 10. Error Handling

Programs should not crash when files are missing.

Use:

```python
try:
    ...
except FileNotFoundError:
    ...
except Exception as e:
    ...
```

# 📌 Modules Used

| Module | Purpose |
|----------|---------|
| `json` | Read JSON files |
| `os` | Handle file paths |
| `collections.Counter` | Count repeated items |

---

# 📖 Example

Reading a JSON file

```python
import json

with open("countries_data.json", "r") as file:
    data = json.load(file)
```

---

Counting lines

```python
lines = 0

for line in file:
    lines += 1
```

---

Counting words

```python
words += len(line.split())
```

---

Sorting

```python
sorted(data, key=lambda x: x["population"], reverse=True)
```

---

# ⚠️ Common Mistakes

### Forgetting UTF-8 encoding

Wrong

```python
open(file)
```

Better

```python
open(file, encoding="utf-8")
```

---

### Forgetting to close files

Instead of

```python
file = open(...)
```

Use

```python
with open(...) as file:
```

---

### Not handling missing files

Always use

```python
try:
    ...
except FileNotFoundError:
```

---

# 📝 Key Takeaways

- File handling allows programs to read external data.
- `with open()` automatically manages file resources.
- `json.load()` converts JSON into Python objects.
- `Counter` efficiently counts repeated values.
- Sorting with `sorted()` and `lambda` helps organize data.
- Exception handling makes programs robust and user-friendly.

---

# 🚀 Skills Practiced

- Reading text files
- Counting lines and words
- Opening JSON files
- Parsing JSON data
- Using `Counter`
- Sorting lists of dictionaries
- Finding the most spoken languages
- Finding the most populated countries
- Handling file-related errors

---

# 💡 Reflection

Today I learned how to work with external files in Python. I practiced reading text files to count lines and words, loading structured data from JSON files, and analyzing large datasets. I also used the `Counter` class to identify the most spoken languages and sorted country data to find the most populated countries. Additionally, I strengthened my understanding of file path handling and exception handling, making my programs more reliable and suitable for real-world data processing.
