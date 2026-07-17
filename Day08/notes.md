# Day 08 - Dictionaries

## 🎯 Topics Covered

- Creating Dictionaries
- Adding Key-Value Pairs
- Accessing Dictionary Values
- Modifying Dictionaries
- Nested Dictionaries
- Dictionary Methods
- Dictionary Keys and Values
- Converting Dictionaries
- Deleting Dictionary Items

---

## 📚 Concepts Learned

### Creating Dictionaries

A dictionary is a collection of key-value pairs. Dictionaries are mutable, unordered (in concept) and allow fast access to data using keys.

Example:

```python
dog = {
    "name": "Tiger",
    "breed": "Dalmatian"
}
```

An empty dictionary can be created using:

```python
dog = {}
```

---

### Adding Key-Value Pairs

New data can be added by assigning a value to a new key.

```python
dog["age"] = 9
```

---

### Accessing Dictionary Values

Dictionary values are accessed using their corresponding keys.

```python
student_dictionary["skills"]
```

---

### Nested Dictionaries

A dictionary can contain another dictionary as one of its values.

Example:

```python
address = {
    "street": "xyz street",
    "pincode": "575101"
}
```

Nested dictionaries help organize related information.

---

### Dictionary Methods

Practiced several useful dictionary methods.

#### `keys()`

Returns all keys in the dictionary.

```python
student_dictionary.keys()
```

---

#### `values()`

Returns all values in the dictionary.

```python
student_dictionary.values()
```

---

#### `items()`

Returns key-value pairs as tuples.

```python
student_dictionary.items()
```

---

### Modifying Dictionary Values

Updated the student's skills by adding a new skill.

```python
skills.append("C")
```

---

### Finding Dictionary Length

Used the built-in function:

```python
len(student_dictionary)
```

to count the number of key-value pairs.

---

### Type Checking

Verified the data type of dictionary values using:

```python
type(skills)
```

---

### Deleting Dictionary Data

Removed a specific key-value pair.

```python
del student_dictionary["skills"]
```

Deleted the entire dictionary.

```python
del student_dictionary
```

---

## 📝 Key Takeaways

- Dictionaries store data as key-value pairs.
- Keys are unique and used to access values.
- Dictionaries are mutable and can be modified after creation.
- Learned how to add, access, update and delete dictionary entries.
- Used dictionary methods like `keys()`, `values()` and `items()`.
- Worked with nested dictionaries to organize structured data.
- Used `len()` and `type()` with dictionaries.

---

## 🛠️ Dictionary Methods Practiced

| Method | Purpose |
|---------|---------|
| `keys()` | Returns all dictionary keys |
| `values()` | Returns all dictionary values |
| `items()` | Returns key-value pairs as tuples |
| `len()` | Returns the number of key-value pairs |
| `type()` | Checks the data type |
| `del` | Deletes a key or the entire dictionary |

---

## 🚀 Skills Practiced

- Dictionaries
- Key-Value Pairs
- Nested Dictionaries
- Dictionary Methods
- Data Access
- Data Modification
- Type Checking
- Built-in Functions
- Data Structures

---

## 💡 Reflection

Today I learned about Python dictionaries, one of the most useful data structures for storing and organizing information. I practiced creating dictionaries, adding and updating key-value pairs, accessing data, working with nested dictionaries, and using common dictionary methods. Understanding dictionaries will help me efficiently manage structured data in future Python projects.
