# Day 10 - Loops

## 🎯 Topics Covered

- for Loop
- while Loop
- Nested Loops
- Pattern Printing
- Iterating Through Lists
- Working with Ranges
- Mathematical Computations
- Data Traversal
- Loop-based Problem Solving

---

## 📚 Concepts Learned

### for Loop

The `for` loop is used to iterate over a sequence such as a list, tuple, string or range.

Example:

```python
for i in range(11):
    print(i)
```

Practiced counting from:

- 0 to 10
- 10 to 0

using both `for` and `while` loops.

---

### while Loop

A `while` loop executes repeatedly as long as its condition remains `True`.

Example:

```python
i = 0

while i <= 10:
    print(i)
    i += 1
```

Learned when a `while` loop is more suitable than a `for` loop.

---

### Pattern Printing

Used loops to generate different text-based patterns.

Examples:

Triangle Pattern

```text
#
##
###
####
#####
######
#######
```

Hash Matrix

```text
# # # # # # #
# # # # # # #
# # # # # # #
...
```

These exercises improved my understanding of nested loops and repeated output.

---

### Multiplication Pattern

Generated a multiplication pattern using loops.

Example:

```text
5 x 5 = 25
```

Used:

```python
for i in range(11):
```

to calculate squares of numbers.

---

### Iterating Through Lists

Traversed a list using a `for` loop.

Example:

```python
languages = [
    'Python',
    'NumPy',
    'Pandas',
    'Django',
    'Flask'
]
```

Printed every element individually.

---

### Even and Odd Numbers

Used loops to print:

- Even numbers
- Odd numbers

Practiced two different approaches:

- Using `range()` with a step value
- Using conditional statements (`if`)

---

### Summation Using Loops

Calculated:

- Sum of numbers from 0 to 100
- Sum of all even numbers
- Sum of all odd numbers

Learned how to use accumulator variables.

Example:

```python
total += i
```

---

### Working with Lists

Solved problems involving lists, including:

- Reversing a list using loops
- Traversing country names
- Working with country datasets

These exercises helped strengthen list manipulation skills.

---

### Nested Loops

Used loops inside another loop to generate repeated patterns.

Example:

```python
for i in range(rows):
    for j in range(columns):
        print("#", end=" ")
```

Nested loops are useful for grids, matrices, and pattern generation.

---

## 📝 Key Takeaways

- Learned the difference between `for` and `while` loops.
- Used `range()` effectively with different start, stop, and step values.
- Practiced nested loops for pattern generation.
- Used loops for mathematical calculations.
- Traversed lists and datasets efficiently.
- Built logic using accumulator variables.
- Strengthened problem-solving skills through loop-based exercises.

---

## 🛠️ Python Features Practiced

| Feature | Purpose |
|---------|---------|
| `for` | Iterate over sequences |
| `while` | Repeat while a condition is true |
| `range()` | Generate sequences of numbers |
| Nested Loops | Work with matrices and patterns |
| `if` | Conditional execution inside loops |
| `+=` | Update accumulator variables |
| `print()` | Display formatted output |

---

## 🚀 Skills Practiced

- for Loops
- while Loops
- Nested Loops
- Pattern Printing
- Iteration
- Mathematical Computation
- List Traversal
- Problem Solving
- Data Processing
- Algorithmic Thinking

---

## 💡 Reflection

Today I explored one of the most fundamental concepts in programming—loops. I practiced using both `for` and `while` loops to automate repetitive tasks, generate patterns, iterate through lists, and perform mathematical calculations. Working with nested loops also helped me understand how complex patterns and structured outputs are created. These exercises strengthened my logical thinking and laid the foundation for solving more advanced programming problems in Python.
