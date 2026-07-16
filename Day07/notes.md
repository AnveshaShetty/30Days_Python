# Day 07 - Sets

## 🎯 Topics Covered

- Creating Sets
- Set Properties
- Adding and Updating Elements
- Set Operations
- Membership Testing
- Removing Elements
- Set Comparison
- Set Methods
- Converting Lists to Sets
- Finding Unique Elements

---

## 📚 Concepts Learned

### Creating Sets

A set is an **unordered collection of unique elements**. Unlike lists and tuples, sets do not allow duplicate values.

Example:

```python
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple'}
```

---

### Set Properties

- Unordered
- Mutable (elements can be added or removed)
- No duplicate values
- Cannot access elements using indexing

---

### Adding Elements

Added a single element using:

```python
it_companies.add('Twitter')
```

Added multiple elements using:

```python
it_companies.update(companies)
```

---

### Set Operations

Practiced common mathematical set operations.

#### Union

Combines all unique elements from two sets.

```python
A.union(B)
```

---

#### Intersection

Returns elements common to both sets.

```python
A.intersection(B)
```

---

#### Symmetric Difference

Returns elements that exist in either set but not in both.

```python
A.symmetric_difference(B)
```

---

#### Subset

Checks whether one set is completely contained within another.

```python
A.issubset(B)
```

---

#### Disjoint Sets

Checks whether two sets have no common elements.

```python
A.isdisjoint(B)
```

---

### Updating Sets

Merged two sets using:

```python
A.update(B)
```

Unlike `union()`, `update()` modifies the original set.

---

### Removing Elements

Used:

```python
remove()
```

and learned the difference between:

| Method | Behavior |
|---------|----------|
| `remove()` | Raises an error if the element does not exist |
| `discard()` | Does nothing if the element does not exist |

---

### Deleting Sets

Deleted entire sets using:

```python
del A
```

---

### Converting Lists to Sets

Converted a list into a set.

```python
set(age)
```

This automatically removed duplicate values.

---

### Comparing Data Structures

Reviewed the characteristics of:

| Data Type | Ordered | Mutable | Duplicates |
|------------|:-------:|:-------:|:----------:|
| String | ✅ | ❌ | ✅ |
| List | ✅ | ✅ | ✅ |
| Tuple | ✅ | ❌ | ✅ |
| Set | ❌ | ✅ | ❌ |

---

### Finding Unique Words

Used:

```python
split()
```

and

```python
set()
```

to determine the number of unique words in a sentence.

This demonstrated a practical use of sets for removing duplicate values.

---

## 📝 Key Takeaways

- Sets store only unique values.
- Duplicate elements are automatically removed.
- Learned mathematical set operations such as union, intersection, and symmetric difference.
- Used `add()` and `update()` to insert elements.
- Understood the difference between `remove()` and `discard()`.
- Converted lists into sets to eliminate duplicates.
- Used sets to count unique words in a sentence.
- Compared strings, lists, tuples, and sets based on their characteristics.

---

## 🛠️ Set Methods Practiced

| Method | Purpose |
|---------|---------|
| `add()` | Add one element |
| `update()` | Add multiple elements |
| `union()` | Combine two sets |
| `intersection()` | Find common elements |
| `issubset()` | Check subset relationship |
| `isdisjoint()` | Check if sets have no common elements |
| `symmetric_difference()` | Find elements present in only one set |
| `remove()` | Remove an element |
| `discard()` | Remove an element safely |
| `set()` | Convert another data type into a set |

---

## 🚀 Skills Practiced

- Sets
- Set Operations
- Set Methods
- Membership Testing
- Data Structure Comparison
- Removing Duplicates
- Type Conversion
- Built-in Functions
- Problem Solving

---

## 💡 Reflection

Today I learned about Python sets and how they are useful for storing unique values and performing mathematical operations efficiently. I practiced creating sets, adding and removing elements, combining sets, checking relationships between sets, and eliminating duplicates from data. I also explored a practical application by finding unique words in a sentence. Understanding sets has improved my knowledge of Python's built-in data structures and when to use each one effectively.
