# Day 06 - Tuples

## 🎯 Topics Covered

- Creating Tuples
- Empty Tuples
- Tuple Concatenation
- Tuple Unpacking
- Tuple Membership
- Tuple to List Conversion
- Tuple Slicing
- Deleting Tuples
- Working with Immutable Data

---

## 📚 Concepts Learned

### Creating Tuples

A tuple is an ordered collection of items that cannot be modified after creation (immutable).

Examples:

```python
fruits = ('banana', 'apple', 'mango')

empty_tuple = ()
```

---

### Tuple Concatenation

Combined multiple tuples using the `+` operator.

```python
food_stuff_tp = fruits + vegetables + animal_products
```

---

### Tuple to List Conversion

Converted a tuple into a list to perform operations that require mutability.

```python
food_stuff_lt = list(food_stuff_tp)
```

Used:

```python
type()
```

to verify the converted data type.

---

### Tuple Slicing

Extracted specific portions of a tuple/list.

Examples:

- Middle item(s)
- First three elements
- Last three elements

```python
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
```

---

### Tuple Membership

Checked whether an item exists inside a tuple using the membership operator.

```python
'Iceland' in nordic_countries
```

```python
'Estonia' in nordic_countries
```

---

### Tuple Unpacking

Used unpacking to separate values from a tuple.

Example:

```python
*siblings, dad, mom = family_members
```

The `*` operator collects multiple values into a list while assigning the remaining values individually.

---

### Deleting a Tuple

Deleted an entire tuple using:

```python
del food_stuff_tp
```

Unlike lists, tuples cannot have individual elements removed because they are immutable.

---

## 📝 Key Takeaways

- Tuples are ordered and immutable collections.
- Multiple tuples can be combined using the `+` operator.
- Tuples can be converted into lists for modification.
- Membership operators (`in`, `not in`) work with tuples.
- Tuple unpacking simplifies extracting multiple values.
- Slicing allows access to specific parts of a tuple.
- Entire tuples can be deleted using the `del` statement.

---

## 🛠️ Tuple Operations Practiced

| Operation | Purpose |
|-----------|---------|
| `+` | Join tuples |
| `list()` | Convert tuple to list |
| `in` | Membership test |
| `not in` | Check absence of an item |
| `del` | Delete a tuple |
| Slicing (`[:]`) | Extract elements |
| Tuple Unpacking (`*`) | Assign multiple values |

---

## 🚀 Skills Practiced

- Tuples
- Tuple Concatenation
- Tuple Unpacking
- Tuple Slicing
- Membership Operators
- Type Conversion
- Immutable Data Structures
- Built-in Functions
- Problem Solving

---

## 💡 Reflection

Today I learned about Python tuples and how they differ from lists. I practiced creating tuples, joining them, checking for elements, unpacking values, converting tuples into lists, and working with immutable data. Understanding tuples helps in situations where data should remain unchanged and provides a solid foundation for working with different Python data structures.
