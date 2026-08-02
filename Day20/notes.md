# Day 20 - Python Modules, Packages & Library Installation

# 🎯 Topics Covered

- Python Modules
- Creating Custom Modules
- Importing Modules
- Python Packages
- `__init__.py`
- Installing Packages using pip
- NumPy Basics
- Pandas Installation
- Webbrowser Module
- Requests Module
- Git Commit & Push

---

# 📚 Introduction

As programs become larger, writing everything in a single file becomes difficult to manage. Python solves this problem using **modules** and **packages**, allowing code to be divided into reusable files.

Today focused on creating custom modules, importing them into another program, installing third-party libraries using `pip`, and experimenting with popular packages like **NumPy**, **Pandas**, and **Requests**.

---

# 1. What is a Module?

A **module** is simply a Python file (`.py`) containing functions, variables, or classes that can be reused in other Python programs.

Example:

```
arithmatic.py
greet.py
```

Instead of rewriting the same functions repeatedly, they can be imported whenever needed.

---

# 2. Creating a Custom Module

Created a file named:

```
arithmatic.py
```

It contains several arithmetic functions:

- Addition
- Subtraction
- Multiplication
- Division
- Remainder
- Power

The functions include `add_numbers()`, `subtract()`, `multiple()`, `division()`, `remainder()`, and `power()`.

---

# 3. Creating Another Module

Created another module:

```
greet.py
```

This module contains a greeting function:

```python
greet_person(firstname, lastname)
```

which returns a welcome message using the provided first and last names. 

---

# 4. Importing Modules

Modules can be imported using the `import` keyword.

Example:

```python
import arithmatic
import greet
```

After importing, functions are called using:

```python
arithmatic.add_numbers(...)
greet.greet_person(...)
```

Your `sum.py` program imports both modules, performs arithmetic operations, and prints a greeting message.

---

# 5. Package Structure

A package is a collection of related modules stored inside a folder.

Example:

```
Day20/
│
├── __init__.py
├── arithmatic.py
├── greet.py
└── sum.py
```

The `__init__.py` file tells Python that the directory should be treated as a package.

---

# 6. Installing Python Packages

Python packages can be installed using **pip**.

Check pip version:

```bash
pip --version
```

Install a package:

```bash
pip install numpy
```

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Install another package:

```bash
pip install pandas
```

---

# 7. NumPy

NumPy is the most popular Python library for numerical computing.

Import:

```python
import numpy
```

Create an array:

```python
numbers = [1,2,3,4,5]

array = numpy.array(numbers)
```

Output

```
array([1,2,3,4,5])
```

NumPy supports vectorized operations:

```python
array * 2
```

Output

```
[2 4 6 8 10]
```

Adding a scalar:

```python
array + 2
```

Output

```
[3 4 5 6 7]
```

Unlike Python lists, NumPy performs mathematical operations on every element efficiently.

---

# 8. Pandas

Pandas is a Python library used for data analysis.

Installation:

```bash
pip install pandas
```

Import:

```python
import pandas
```

Pandas is commonly used for:

- Reading CSV files
- Reading Excel files
- Data cleaning
- Data analysis
- Data visualization (with other libraries)

---

# 9. webbrowser Module

Python provides a built-in module called:

```python
import webbrowser
```

It can automatically open URLs in the default browser.

Example:

```python
url_list = [
    "http://www.python.org",
    "https://github.com/AnveshaShetty"
]

for url in url_list:
    webbrowser.open_new_tab(url)
```

This opens each website in a new browser tab.

---

# 10. Requests Module

The `requests` library is used for sending HTTP requests.

Install:

```bash
pip install requests
```

Example:

```python
import requests

url = "https://example.com"

response = requests.get(url)
```

Useful properties:

```python
response.status_code
response.headers
response.text
```

While testing, the requested W3C URL returned an HTTP **404 (Page Not Found)** response, demonstrating how to inspect the status code, headers, and returned HTML.

---

# 11. Git Workflow

After completing the program:

Stage files:

```bash
git add .
```

Commit:

```bash
git commit -m "Added sum.py file to perform calculation"
```

Push:

```bash
git push
```

Successfully pushed the Day 20 work to GitHub.

---

# 📌 Important Concepts

| Concept | Purpose |
|----------|---------|
| Module | Reusable Python file |
| Package | Collection of modules |
| `import` | Use code from another module |
| `pip` | Install external libraries |
| NumPy | Numerical computing |
| Pandas | Data analysis |
| Requests | HTTP requests |
| webbrowser | Open URLs in browser |

---

# 📖 Examples

Import module

```python
import arithmatic
```

---

Call function

```python
arithmatic.add_numbers(1,2,3)
```

---

Import greeting module

```python
import greet
```

---

Call greeting

```python
greet.greet_person("Anvesha", "Pratham")
```

---

Install package

```bash
pip install numpy
```

---

Install pandas

```bash
pip install pandas
```

---

Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

NumPy array

```python
import numpy

arr = numpy.array([1,2,3])
```

---

Open websites

```python
import webbrowser

webbrowser.open_new_tab("https://python.org")
```

---

HTTP Request

```python
import requests

response = requests.get(url)
print(response.status_code)
```

---

# ⚠️ Common Mistakes

### Forgetting to install packages

Wrong

```python
import numpy
```

without installation.

Correct

```bash
pip install numpy
```

---

### Forgetting module name

Wrong

```python
add_numbers()
```

Correct

```python
arithmatic.add_numbers()
```

---

### Missing `__init__.py`

Without it, Python may not recognize the folder as a package in some contexts.

---

### Import Errors

Ensure the module file is in the same directory (or package) before importing it.

---

# 📝 Key Takeaways

- Modules make programs reusable and organized.
- Packages group related modules together.
- `__init__.py` marks a directory as a package.
- `pip` installs third-party libraries.
- NumPy provides fast mathematical operations on arrays.
- Pandas is widely used for data analysis.
- The `webbrowser` module can launch web pages.
- The `requests` library retrieves web content using HTTP.
- Git helps track and upload project changes to GitHub.

---

# 🚀 Skills Practiced

- Creating custom modules
- Importing modules
- Creating Python packages
- Installing packages with pip
- Using NumPy arrays
- Installing and importing Pandas
- Opening websites using `webbrowser`
- Sending HTTP requests using `requests`
- Committing and pushing code with Git

---

# 💡 Reflection

Today I learned how to organize Python programs using modules and packages, making my code more reusable and easier to maintain. I created custom modules for arithmetic operations and greetings, imported them into another program, and practiced executing them successfully. I also installed external libraries such as NumPy and Pandas using `pip`, explored NumPy's array operations, experimented with the `webbrowser` and `requests` modules, and completed the workflow by committing and pushing my project to GitHub.
