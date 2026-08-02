# Day 17 - Exception Handling & List Unpacking

# 🎯 Topics Covered

- Exception Handling
- Types of Errors
- try-except Block
- else Clause
- finally Clause
- Raising Exceptions
- List Unpacking
- Multiple Variable Assignment
- Star (`*`) Operator

---

# 📚 Introduction

Errors are a normal part of programming. Instead of letting a program crash, Python allows us to **handle exceptions gracefully** using `try` and `except`.

Day 17 also introduced **list unpacking**, where elements of a list can be assigned directly to variables.

---

# 1. What is an Exception?

An **exception** is an error that occurs while the program is running.

Example:

```python
print(10 / 0)
```

Output

```
ZeroDivisionError
```

Without exception handling, the program stops immediately.

---

# 2. Common Python Exceptions

| Exception | Cause |
|-----------|------|
| `NameError` | Variable not defined |
| `TypeError` | Invalid operation between data types |
| `ValueError` | Invalid value passed |
| `IndexError` | Invalid list index |
| `KeyError` | Dictionary key not found |
| `ImportError` | Cannot import module/object |
| `AttributeError` | Object has no attribute |
| `ZeroDivisionError` | Division by zero |
| `FileNotFoundError` | File doesn't exist |

---

# 3. Handling Exceptions

Basic Syntax

```python
try:
    code
except:
    error handling
```

Example

```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

Output

```
Cannot divide by zero.
```

Instead of crashing, Python executes the `except` block.

---

# 4. Handling Multiple Exceptions

```python
try:
    number = int(input())
    print(10 / number)

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")
```

Each exception can be handled separately.

---

# 5. Using Exception Objects

```python
try:
    print(10 / 0)

except Exception as e:
    print(e)
```

Output

```
division by zero
```

`e` stores the actual error message.

---

# 6. else Block

Runs only when no exception occurs.

```python
try:
    number = 5

except:
    print("Error")

else:
    print("Everything is fine")
```

Output

```
Everything is fine
```

---

# 7. finally Block

Runs whether an exception occurs or not.

```python
try:
    print("Program Started")

finally:
    print("Program Finished")
```

Output

```
Program Started
Program Finished
```

Useful for:

- Closing files
- Database connections
- Cleaning resources

---

# 8. Raising Exceptions

Python allows us to create our own errors.

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
```

Output

```
ValueError: Age cannot be negative
```

---

# 9. List Unpacking

Instead of accessing indexes individually:

```python
countries = ["India", "Japan", "Germany"]
```

Normal way

```python
print(countries[0])
print(countries[1])
```

Unpacking

```python
country1, country2, country3 = countries
```

Now

```python
print(country1)
```

Output

```
India
```

---

# 10. Using the Star Operator

The `*` operator collects remaining items.

Example

```python
numbers = [1,2,3,4,5]

first, *middle, last = numbers

print(first)
print(middle)
print(last)
```

Output

```
1
[2,3,4]
5
```

---

# 11. Nordic Countries Exercise

Given

```python
names = [
    "Finland",
    "Sweden",
    "Norway",
    "Denmark",
    "Iceland",
    "Estonia",
    "Russia"
]
```

Result

```python
nordic_countries

['Finland',
 'Sweden',
 'Norway',
 'Denmark',
 'Iceland']

es = "Estonia"

ru = "Russia"
```

---

# 📌 Exception Handling Syntax

```python
try:
    code

except ExceptionType:
    handle error

else:
    execute if no error

finally:
    always execute
```

---

# 📌 Common Error Messages

| Error | Meaning |
|--------|---------|
| NameError | Variable not defined |
| ValueError | Wrong value |
| IndexError | Invalid index |
| KeyError | Dictionary key missing |
| TypeError | Wrong data type |
| ImportError | Module cannot be imported |
| ZeroDivisionError | Cannot divide by zero |

---

# 📝 Key Takeaways

- Exceptions prevent programs from crashing.
- `try` contains risky code.
- `except` handles errors.
- `else` runs only if no exception occurs.
- `finally` always executes.
- `raise` creates custom exceptions.
- List unpacking assigns list elements directly to variables.
- `*` collects multiple remaining elements.

---

# 🚀 Skills Practiced

- Understanding Python exceptions
- Writing `try-except` blocks
- Using `else` and `finally`
- Raising custom exceptions
- List unpacking
- Using the star (`*`) operator
- Working with multiple assignment

---

# 💡 Reflection

Today I learned how to make Python programs more reliable by handling runtime errors using exception handling. I explored different exception types, learned how `try`, `except`, `else`, and `finally` work together, and understood when to raise custom exceptions. I also practiced list unpacking and the star (`*`) operator, making it easier to assign multiple values from a list in a clean and readable way.
