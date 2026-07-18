# Day 09 - Conditionals

## 🎯 Topics Covered

- Conditional Statements
- Comparison Operators
- Logical Operators
- Nested Conditions
- User Input
- Membership Operators
- Decision Making
- Working with Dictionaries
- Real-world Conditional Problems

---

## 📚 Concepts Learned

### Conditional Statements

Conditional statements allow a program to make decisions based on whether a condition is `True` or `False`.

Basic syntax:

```python
if condition:
    # code

elif another_condition:
    # code

else:
    # code
```

---

### Comparison Operators

Used comparison operators to compare values.

Examples:

```python
==
!=
>
<
>=
<=
```

Example:

```python
if age >= 18:
    print("You are old enough to drive")
```

---

### Logical Operators

Combined multiple conditions using logical operators.

```python
and
or
not
```

Example:

```python
if person['is_married'] and person['country'] == 'Finland':
```

---

### User Input

Collected user input using:

```python
input()
```

Converted string input into integers using:

```python
int(input())
```

Used input in several real-life scenarios:

- Driving eligibility
- Age comparison
- Number comparison
- Student grading
- Fruit checker

---

### Nested Conditions

Placed one `if` statement inside another.

Example:

```python
if my_age < your_age:
    if diff == 1:
        print("1 year difference!")
```

Nested conditions make it possible to handle more complex decision-making.

---

### Membership Operators

Checked whether an item exists inside a list or dictionary.

Examples:

```python
fruit in fruits

"skills" in person

"Python" in person["skills"]
```

---

### Dictionary Conditions

Worked with a dictionary containing personal information.

Practiced:

- Checking whether a key exists
- Accessing nested values
- Working with list values inside dictionaries

Example:

```python
if "skills" in person:
```

---

### String Formatting

Used formatted strings to display readable output.

Example:

```python
print(f"You need {diff} more years to learn to drive.")
```

---

## 📝 Key Takeaways

- Learned how Python makes decisions using `if`, `elif`, and `else`.
- Practiced using comparison and logical operators.
- Used nested conditions to solve more complex problems.
- Took user input and processed it using conditional logic.
- Worked with dictionaries and lists inside conditions.
- Used membership operators to check for items.
- Improved problem-solving through real-life programming exercises.

---

## 🛠️ Python Features Practiced

| Feature | Purpose |
|---------|---------|
| `if` | Execute code when a condition is true |
| `elif` | Check additional conditions |
| `else` | Execute when all previous conditions are false |
| `input()` | Take user input |
| `int()` | Convert input to integer |
| `in` | Membership testing |
| `and` | Combine conditions |
| `or` | Check multiple possible conditions |
| `not` | Reverse a condition |
| `len()` | Find the length of a list |
| `abs()` | Calculate absolute difference |

---

## 🚀 Skills Practiced

- Conditional Statements
- Decision Making
- User Input
- Comparison Operators
- Logical Operators
- Nested Conditions
- Membership Operators
- Dictionaries
- Lists
- Problem Solving

---

## 💡 Reflection

Today I learned how to make Python programs think and make decisions using conditional statements. I practiced solving real-world problems by combining user input, comparison operators, logical operators, and dictionaries. I also worked with nested conditions and membership testing, which helped me write more dynamic and interactive programs. Understanding conditionals is an important step toward building intelligent and responsive applications.
