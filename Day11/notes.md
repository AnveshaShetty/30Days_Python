# Day 11 - Functions

## 🎯 Topics Covered

- Introduction to Functions
- Defining Functions
- Function Parameters
- Variable-Length Arguments (`*args`)
- Calling Functions
- Iterating Through Function Arguments

---

## 📚 Concepts Learned

### What is a Function?

A function is a reusable block of code that performs a specific task. Functions help make programs more organized, readable, and reusable.

General syntax:

```python
def function_name(parameters):
    # code
```

---

### Defining a Function

Functions are created using the `def` keyword.

Example:

```python
def greet():
    print("Hello!")
```

---

### Function Parameters

Parameters allow us to pass data into a function.

Example:

```python
def greet(name):
    print(f"Hello {name}")
```

---

### Variable-Length Arguments (`*args`)

Using `*args` allows a function to accept any number of arguments.

Example:

```python
def print_list(*items):
    for item in items:
        print(item)
```

This is useful when the number of inputs is unknown.

---

### Calling a Function

A function runs only when it is called.

Example:

```python
print_list("mango", "apple", "strawberry")
```

Output:

```text
mango
apple
strawberry
```

---

### Using Loops Inside Functions

Functions can contain loops to process multiple values efficiently.

Example:

```python
for item in items:
    print(item)
```

This prints every element passed to the function.

---

## 📝 Key Takeaways

- Learned how to create user-defined functions.
- Understood the purpose of parameters.
- Learned how `*args` accepts multiple arguments.
- Combined loops with functions.
- Practiced calling functions with different inputs.
- Improved code reusability and organization.

---

## 🛠️ Python Features Practiced

| Feature | Purpose |
|---------|---------|
| `def` | Define a function |
| `*args` | Accept multiple arguments |
| `for` | Iterate through arguments |
| `print()` | Display output |
| Function Call | Execute a function |

---

## 🚀 Skills Practiced

- User-defined Functions
- Function Parameters
- Variable-Length Arguments
- Looping
- Code Reusability
- Python Fundamentals

---

## 💡 Reflection

Today I began learning one of the most important concepts in Python—functions. I learned how to define my own functions, pass arguments to them, and use loops inside functions to process multiple values. Understanding functions will help me write cleaner, reusable, and more organized code as I continue my Python learning journey.
