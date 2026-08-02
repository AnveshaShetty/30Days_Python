# Day 16 - Python Date & Time
---

# 🎯 Topics Covered

- `datetime` module
- Current Date & Time
- Unix Timestamp
- Formatting Dates (`strftime`)
- Converting String to Date (`strptime`)
- Date Arithmetic
- Calculating Time Difference

---

# 📚 Introduction

Python provides the **datetime** module to work with dates and times.

It helps in:

- Getting current date and time
- Formatting dates
- Parsing date strings
- Calculating time differences
- Working with timestamps

---

# 📦 Importing datetime

```python
from datetime import datetime
```

or

```python
import datetime
```

---

# 1. Getting Current Date & Time

Use `datetime.now()` to retrieve the current system date and time.

Example:

```python
from datetime import datetime

current_date = datetime.now()

print(current_date)
```

Output

```
2026-07-26 13:31:20.153462
```

This returns a **datetime object** containing:

- Year
- Month
- Day
- Hour
- Minute
- Second
- Microsecond

Your implementation retrieves the current date and stores it in `current_date`. :contentReference[oaicite:0]{index=0}

---

# 2. Unix Timestamp

A timestamp represents the number of seconds that have passed since:

```
1 January 1970
```

Example:

```python
timestamp = current_date.timestamp()

print(timestamp)
```

Output

```
1785052880.153462
```

Useful for:

- Databases
- APIs
- Logging
- Authentication
- Time comparisons

My code uses the `timestamp()` method to generate the Unix timestamp. :contentReference[oaicite:1]{index=1}

---

# 3. Formatting Dates

Python formats dates using the `strftime()` method.

Syntax

```python
date.strftime(format)
```

Common format codes:

| Code | Meaning |
|------|---------|
| `%d` | Day |
| `%m` | Month |
| `%Y` | Year |
| `%H` | Hour (24-hour) |
| `%M` | Minute |
| `%S` | Second |
| `%B` | Full Month Name |
| `%A` | Weekday Name |

Example

```python
formatted = current_date.strftime("%m/%d/%Y, %H:%M:%S")

print(formatted)
```

Output

```
07/26/2026, 13:31:20
```

---

# 4. Converting String to Date

Sometimes dates are stored as strings.

Python converts them using:

```python
datetime.strptime()
```

Example

```python
from datetime import datetime

date_string = "5 December, 2019"

date = datetime.strptime(date_string, "%d %B, %Y")

print(date)
```

Output

```
2019-12-05 00:00:00
```

Here:

- `%d` → Day
- `%B` → Month Name
- `%Y` → Year

My solution correctly parses the string into a datetime object. :contentReference[oaicite:3]{index=3}

---

# 5. Calculating Time Difference

Dates can be subtracted directly.

Example

```python
difference = future_date - today
```

The result is a **timedelta** object.

---

## Time Until New Year

Example

```python
today = date(2026, 7, 26)
new_year = date(2027, 1, 1)

difference = new_year - today

print(difference)
```

Output

```
159 days, 0:00:00
```

My program calculates the remaining time until New Year. :contentReference[oaicite:4]{index=4}

---

## Days Since Unix Epoch

Example

```python
epoch = date(1970, 1, 1)

today = date.today()

difference = today - epoch
```

Output

```
20660 days
```

My implementation calculates the number of days between 1 January 1970 and the selected date. :contentReference[oaicite:5]{index=5}

---

# 📌 Important datetime Methods

| Method | Purpose |
|---------|---------|
| `datetime.now()` | Current date & time |
| `date.today()` | Current date |
| `timestamp()` | Unix timestamp |
| `strftime()` | Format date |
| `strptime()` | Convert string to date |

---

# 📖 Common Format Specifiers

| Specifier | Meaning |
|-----------|---------|
| `%d` | Day (01-31) |
| `%m` | Month (01-12) |
| `%Y` | Four-digit year |
| `%y` | Two-digit year |
| `%H` | Hour (24-hour) |
| `%I` | Hour (12-hour) |
| `%M` | Minute |
| `%S` | Second |
| `%A` | Weekday name |
| `%a` | Short weekday |
| `%B` | Full month name |
| `%b` | Short month name |

---

# ⚠️ Common Mistakes

### ❌ Using `timestamp()` for formatting

Wrong

```python
current_date.timestamp("%m/%d/%Y")
```

Correct

```python
current_date.strftime("%m/%d/%Y")
```

---

### ❌ Wrong format string

```python
datetime.strptime(date, "%Y/%d/%m")
```

If the string format doesn't match exactly, Python raises a `ValueError`.

---

# 📝 Key Takeaways

- `datetime` module handles dates and times.
- `datetime.now()` returns the current date and time.
- `timestamp()` gives Unix time in seconds.
- `strftime()` converts dates into formatted strings.
- `strptime()` converts strings into datetime objects.
- Subtracting two dates returns a `timedelta`.

---

# 🚀 Skills Practiced

- Importing the `datetime` module
- Working with current date and time
- Formatting dates
- Parsing date strings
- Calculating date differences
- Understanding timestamps

---

# 💡 Reflection

Today I learned how Python works with dates and time using the `datetime` module. I practiced retrieving the current date and time, generating Unix timestamps, formatting dates using `strftime()`, converting strings into date objects with `strptime()`, and calculating differences between two dates. These concepts are widely used in logging systems, scheduling applications, data processing, and real-world software development.
