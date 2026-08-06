# Day 25 - Pandas Series & DataFrames

# 🎯 Topics Covered

- Introduction to Pandas
- Pandas Series
- Creating Series
- Custom Index
- Series from Dictionary
- Constant Series
- Series using NumPy Linspace
- DataFrames
- Creating DataFrames
- Reading CSV Files
- DataFrame Properties
- Adding Columns
- Updating Columns
- Calculating BMI
- Data Types in Pandas

---

# 📚 Introduction

**Pandas** is one of Python's most popular libraries for data analysis and manipulation.

It provides two primary data structures:

- **Series** → One-dimensional labeled array.
- **DataFrame** → Two-dimensional table (rows and columns).

Pandas is built on top of **NumPy**, making it fast and efficient for handling structured data.

---

# 1. Importing Pandas

```python
import pandas as pd
import numpy as np
```

- `pandas` → Data analysis
- `numpy` → Numerical operations

The examples begin by importing both libraries. 

---

# 2. Pandas Series

A **Series** is a one-dimensional labeled array capable of holding different data types.

Example:

```python
numbers = [1,2,3,4,5]

series = pd.Series(numbers)
```

Output

```
0    1
1    2
2    3
3    4
4    5
dtype: int64
```

---

# 3. Series with Custom Index

Instead of the default index starting from 0, you can define your own.

```python
fruits = ['Orange','Banana','Mango']

series = pd.Series(fruits, index=[1,2,3])
```

Output

```
1    Orange
2    Banana
3    Mango
```

The uploaded example demonstrates creating a Series with custom indices. 

---

# 4. Series from Dictionary

```python
dictionary = {
    'name':'Anvesha',
    'country':'India',
    'city':'Mangalore'
}

series = pd.Series(dictionary)
```

Each dictionary key becomes the index.

---

# 5. Constant Series

A Series can contain the same value for every index.

```python
series = pd.Series(10, index=[1,2,3])
```

Output

```
1    10
2    10
3    10
```
---

# 6. Series using NumPy Linspace

`linspace()` creates evenly spaced values.

```python
np.linspace(start, stop, number_of_values)
```

Example

```python
series = pd.Series(
    np.linspace(5,20,10)
)
```

This creates ten equally spaced numbers from 5 to 20.

---

# 7. DataFrames

A **DataFrame** is a table consisting of

- Rows
- Columns

Similar to an Excel spreadsheet.

---

# 8. Creating DataFrame from List of Lists

Example

```python
data = [
    ['Asabeneh','Finland','Helsinki'],
    ['David','UK','London'],
    ['John','Sweden','Stockholm']
]

df = pd.DataFrame(
    data,
    columns=['Name','Country','City']
)
```

---

# 9. Creating DataFrame from Dictionary

```python
data = {
    'Name':['Asabeneh','David','John'],
    'Country':['Finland','UK','Sweden'],
    'City':['Helsinki','London','Stockholm']
}

df = pd.DataFrame(data)
```

Each key becomes a column.

---

# 10. Creating DataFrame from List of Dictionaries

```python
data = [
    {'Name':'Asabeneh',
     'Country':'Finland',
     'City':'Helsinki'},

    {'Name':'David',
     'Country':'UK',
     'City':'London'}
]

df = pd.DataFrame(data)
```

Each dictionary represents one row.

---

# 11. Reading CSV Files

CSV stands for

**Comma Separated Values**

Pandas reads CSV files using

```python
df = pd.read_csv("employees.csv")
```

The program shows inspecting the dataset with `head()`, `tail()`, `shape`, and `columns`.

---

# 12. Viewing First Rows

```python
df.head()
```

Displays

First five rows.

---

# 13. Viewing Last Rows

```python
df.tail()
```

Displays

Last five rows.

---

# 14. Shape of DataFrame

```python
df.shape
```

Returns

```
(rows, columns)
```

Example

```
(1000,8)
```

---

# 15. Column Names

```python
df.columns
```

Returns

```
Index(['Name','Country',...])
```

---

# 16. Creating DataFrame from List of Dictionaries

Example

```python
data = [
    {
        "Name":"Asabeneh",
        "Country":"Finland",
        "City":"Helsinki"
    },
    {
        "Name":"David",
        "Country":"UK",
        "City":"London"
    },
    {
        "Name":"John",
        "Country":"Sweden",
        "City":"Stockholm"
    }
]

df = pd.DataFrame(data)
```

The uploaded `dataframe.py` follows this approach.

---

# 17. Adding New Columns

Example

```python
weights = [74,78,69]

df["Weight"] = weights
```

Creates a new column named

```
Weight
```

---

# 18. Updating Existing Columns

Example

```python
df["Height"] = df["Height"] * 0.01
```

Converts

```
173 cm
```

into

```
1.73 m
```

---

# 19. Calculating BMI

Formula

```
BMI = Weight / Height²
```

Example

```python
BMI = weight / (height * height)
```

The program calculates BMI for each person using a function and stores the values in a list.

---

# 20. Adding BMI Column

```python
df["BMI"] = bmi
```

Creates

```
BMI
```

column.

Then

```python
df["BMI"] = round(df["BMI"],1)
```

Rounds values to one decimal place.

---

# 21. Data Types

```python
print(df.Weight.dtype)
```

Output

```
int64
```

Used to check the datatype of a column.

---

# 📊 Workflow

```
Python Data
      │
      ▼
Pandas Series
      │
      ▼
Pandas DataFrame
      │
      ▼
Add Columns
      │
      ▼
Modify Data
      │
      ▼
Analyze Data
```

---

# 📌 Common Pandas Series Functions

| Function | Purpose |
|-----------|----------|
| pd.Series() | Create Series |
| index | Custom indexing |
| dtype | Data type |
| np.linspace() | Evenly spaced values |

---

# 📌 Common DataFrame Functions

| Function | Purpose |
|-----------|----------|
| pd.DataFrame() | Create DataFrame |
| pd.read_csv() | Read CSV file |
| head() | First 5 rows |
| tail() | Last 5 rows |
| shape | Rows and columns |
| columns | Column names |
| dtype | Data type |

---

# 📌 DataFrame Operations

| Operation | Example |
|------------|----------|
| Add column | `df['Age']=age` |
| Modify column | `df['Height']*=0.01` |
| New calculated column | `df['BMI']=bmi` |
| Round values | `round(df['BMI'],1)` |

---

# ⚠️ Common Mistakes

### Forgetting Pandas Import

❌

```python
DataFrame(data)
```

✅

```python
import pandas as pd

pd.DataFrame(data)
```

---

### Reading CSV from Wrong Directory

❌

```python
pd.read_csv("employees.csv")
```

(File not found)

✅

Run the terminal in the folder containing the CSV file or provide the correct file path.

---

### Incorrect BMI Formula

❌

```python
weight / height
```

✅

```python
weight / (height * height)
```

---

### Forgetting to Assign a New Column

❌

```python
round(df["BMI"],1)
```

✅

```python
df["BMI"] = round(df["BMI"],1)
```

---

# 🚀 Skills Practiced

- Working with Pandas
- Creating Series
- Custom indexing
- Dictionary to Series conversion
- Creating DataFrames
- Reading CSV files
- Viewing dataset information
- Adding columns
- Updating column values
- Performing calculations
- Creating derived columns
- Checking data types

---

# 📝 Key Takeaways

- Pandas is the standard Python library for data analysis.
- A **Series** is a one-dimensional labeled array.
- A **DataFrame** is a two-dimensional table with rows and columns.
- DataFrames can be created from lists, dictionaries, or lists of dictionaries.
- CSV files can be loaded using `pd.read_csv()`.
- Columns can be added or modified easily.
- Calculated values, such as BMI, can be stored as new columns.
- Pandas provides useful methods like `head()`, `tail()`, `shape`, `columns`, and `dtype` for inspecting data.

---

# 💡 Reflection

Today I learned the fundamentals of **Pandas**, including how to create and manipulate **Series** and **DataFrames**. I practiced building DataFrames from different data structures, reading data from CSV files, adding and updating columns, computing BMI values, and inspecting datasets using built-in Pandas methods. These skills are essential for data analysis, preprocessing, and machine learning workflows.
