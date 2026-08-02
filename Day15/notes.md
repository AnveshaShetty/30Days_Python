# Day 15 - Python Exception Handling & Common Errors

## 🎯 Topics Covered

- Exceptions in Python
- Runtime Errors
- Syntax Errors
- Common Built-in Exceptions
- Reading Python Tracebacks
- Debugging Techniques

---

# 📚 What is an Exception?

An **exception** is an error that occurs while a program is running.

When Python encounters an exception, it immediately stops executing the current statement and displays an error message called a **Traceback**.

Example:

```python
10 / 0
```

Output:

```
ZeroDivisionError: division by zero
```

---

# Anatomy of a Traceback

Example:

```python
10 / 0
```

Output

```
Traceback (most recent call last):
File "<stdin>", line 1
ZeroDivisionError: division by zero
```

Meaning:

- **Traceback** → shows where the error occurred.
- **File** → current Python file.
- **Line Number** → line causing the error.
- **Exception Name** → type of error.
- **Message** → explanation.

---

# 1. SyntaxError

Occurs when Python cannot understand your code because it violates Python syntax.

Example:

```python
print "Hello"
```

Output

```
SyntaxError: Missing parentheses in call to 'print'
```

Correct:

```python
print("Hello")
```

Common causes:

- Missing parentheses
- Missing colon (`:`)
- Missing quotes
- Wrong indentation

---

# 2. NameError

Occurs when using a variable that has not been created.

Example:

```python
print(language)
```

Output

```
NameError: name 'language' is not defined
```

Correct:

```python
language = "Python"
print(language)
```

---

# 3. ModuleNotFoundError

Occurs when importing a module that does not exist.

Example:

```python
import functional
```

Output

```
ModuleNotFoundError:
No module named 'functional'
```

Correct:

```python
import math
```

---

# 4. IndexError

Occurs when accessing an index that does not exist.

Example:

```python
fruits = ["banana", "apple", "mango", "strawberry"]

print(fruits[4])
```

Output

```
IndexError: list index out of range
```

Correct:

```python
print(fruits[3])
```

---

# 5. KeyError

Occurs when accessing a dictionary key that doesn't exist.

Example:

```python
user = {
    "name": "Anvesha",
    "age": 20
}

print(user["names"])
```

Output

```
KeyError: 'names'
```

Correct:

```python
print(user["name"])
```

---

# 6. TypeError

Occurs when performing operations on incompatible data types.

Example:

```python
3 + user
```

Output

```
TypeError:
unsupported operand type(s)
```

Another example:

```python
"5" + 10
```

Correct:

```python
int("5") + 10
```

---

# 7. ValueError

Occurs when the value is of the correct type but invalid.

Example:

```python
int("13ad")
```

Output

```
ValueError:
invalid literal for int()
```

Correct:

```python
int("13")
```

---

# 8. AttributeError

Occurs when an object does not have the requested attribute.

Example:

```python
import math

math.PI
```

Output

```
AttributeError:
module 'math' has no attribute 'PI'
```

Correct:

```python
math.pi
```

Python attributes are **case-sensitive**.

---

# 9. ImportError

Occurs when importing something that doesn't exist inside a module.

Example:

```python
from math import power
```

Output

```
ImportError:
cannot import name 'power'
```

Correct:

```python
from math import pow
```

---

# 10. ZeroDivisionError

Occurs when dividing by zero.

Example:

```python
10 / 0
```

Output

```
ZeroDivisionError:
division by zero
```

Correct:

```python
10 / 2
```

---

# Difference Between Errors

| Error | Cause |
|--------|-------|
| SyntaxError | Invalid Python syntax |
| NameError | Variable not defined |
| ModuleNotFoundError | Module not installed/found |
| ImportError | Invalid import from module |
| AttributeError | Attribute doesn't exist |
| IndexError | List index doesn't exist |
| KeyError | Dictionary key doesn't exist |
| TypeError | Wrong data types |
| ValueError | Wrong value |
| ZeroDivisionError | Division by zero |

---

# Reading Error Messages

Whenever Python shows an error:

### Step 1

Read the **last line** first.

Example:

```
KeyError: 'name'
```

This tells you the actual problem.

---

### Step 2

Read the line number.

Example:

```
File "main.py", line 15
```

Go to line 15.

---

### Step 3

Fix the mistake.

Run the program again.

---

# Debugging Tips

✔ Read the error message carefully.

✔ Check spelling.

✔ Check indentation.

✔ Check variable names.

✔ Check list indexes.

✔ Check dictionary keys.

✔ Check imported modules.

✔ Print variable values using:

```python
print(variable)
```

✔ Check data types using:

```python
print(type(variable))
```

---

# Useful Functions

```python
type()

len()

print()

help()

dir()
```

These help identify problems during debugging.

---

# Best Practices

- Give meaningful variable names.
- Read the traceback from bottom to top.
- Don't ignore error messages.
- Test code in small parts.
- Keep syntax consistent.
- Use lowercase module attributes (e.g., `math.pi`).

---

# 📝 Key Takeaways

- Exceptions stop program execution.
- Every exception has a specific meaning.
- Python provides detailed tracebacks for debugging.
- Reading the last line of the traceback usually reveals the root cause.
- Learning common exceptions makes debugging much easier.

---

# 🚀 Skills Practiced

- Debugging Python code
- Reading Tracebacks
- Fixing Syntax Errors
- Working with Lists
- Working with Dictionaries
- Importing Modules
- Understanding Data Types
- Exception Identification

---

# 💡 Reflection

Today I learned about Python exceptions and how to debug programs using tracebacks. I explored common errors such as `SyntaxError`, `NameError`, `IndexError`, `KeyError`, `TypeError`, `ValueError`, `AttributeError`, `ImportError`, `ModuleNotFoundError`, and `ZeroDivisionError`. Understanding why these errors occur and how to fix them has improved my confidence in debugging Python code. I also learned that reading the traceback carefully is one of the most valuable skills for solving programming problems.
