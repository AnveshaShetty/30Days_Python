# Day 22 - Web Scraping with Requests & BeautifulSoup

# 🎯 Topics Covered

- Introduction to Web Scraping
- Installing Required Libraries
- HTTP Requests using `requests`
- HTTP Status Codes
- Parsing HTML using BeautifulSoup
- HTML Parser
- Accessing HTML Elements
- Extracting Page Title
- Extracting Page Body
- Finding HTML Tags
- `find_all()` Method

---

# 📚 Introduction

Web Scraping is the process of automatically collecting information from websites using Python.

In today's project, I used:

- `requests` → To download the webpage.
- `BeautifulSoup` → To parse HTML and extract information.

The practice website used was:

```
https://www.scrapethissite.com/pages/simple/
```

which is a sandbox website designed specifically for learning web scraping. 

---

# 1. Installing Required Libraries

Before scraping, install the required packages.

```bash
pip install requests
pip install beautifulsoup4
```

These packages provide tools for downloading web pages and parsing HTML. 

---

# 2. requests Module

The `requests` library is used to send HTTP requests to websites.

Import:

```python
import requests
```

Example:

```python
response = requests.get(url)
```

This sends a GET request and downloads the webpage.

---

# 3. BeautifulSoup

BeautifulSoup reads HTML code and converts it into a searchable Python object.

Import:

```python
from bs4 import BeautifulSoup
```

Create a BeautifulSoup object:

```python
soup = BeautifulSoup(content, "html.parser")
```

Here:

- `content` → HTML received from the website.
- `"html.parser"` → Built-in HTML parser.

---

# 4. Target Website

```python
url = "https://www.scrapethissite.com/pages/simple/"
```

This webpage contains information about countries and is intended for practicing web scraping.

---

# 5. Downloading a Webpage

```python
response = requests.get(url)
```

The downloaded page is stored in the `response` object.

---

# 6. HTTP Status Code

Every request returns a status code.

Example:

```python
status = response.status_code

print(status)
```

Output:

```
200
```

Meaning:

| Code | Meaning |
|-------|----------|
| 200 | Success |
| 404 | Page Not Found |
| 500 | Internal Server Error |
| 403 | Forbidden |

Your program successfully received **200**, meaning the page loaded correctly. 

---

# 7. HTML Content

The HTML source of the webpage is stored in:

```python
content = response.content
```

This raw HTML is then passed to BeautifulSoup for parsing. 

---

# 8. Parsing HTML

```python
soup = BeautifulSoup(content, "html.parser")
```

BeautifulSoup organizes the HTML into a tree structure, allowing easy navigation and searching.

---

# 9. Extracting the Title Tag

Display the `<title>` element:

```python
print(soup.title)
```

Output:

```html
<title>Countries of the World: A Simple Example | Scrape This Site | A public sandbox for learning web scraping</title>
```

---

# 10. Extracting Only the Title Text

To remove HTML tags:

```python
print(soup.title.get_text())
```

Output:

```
Countries of the World: A Simple Example | Scrape This Site | A public sandbox for learning web scraping
```

`get_text()` returns only the readable text inside the HTML element. 

---

# 11. Extracting the Body

```python
print(soup.body)
```

This prints the complete `<body>` section of the webpage, including all nested HTML elements. 

---

# 12. Finding HTML Tags

BeautifulSoup provides methods to search HTML elements.

Example:

```python
image = soup.find_all("img")
```

This finds every `<img>` tag on the page. 

---

# 13. find_all()

Syntax:

```python
find_all(tag_name)
```

Example:

```python
soup.find_all("img")
```

Returns a list containing all matching elements.

Example Output:

```python
[
<img ...>,
<img ...>,
<img ...>
]
```

---

# 14. Important BeautifulSoup Methods

### Access Title

```python
soup.title
```

---

### Get Text

```python
soup.title.get_text()
```

---

### Access Body

```python
soup.body
```

---

### Find All Tags

```python
soup.find_all("img")
```

---

# 15. Complete Program Flow

```
Website URL
      │
      ▼
requests.get()
      │
      ▼
Response Object
      │
      ▼
response.content
      │
      ▼
BeautifulSoup
      │
      ▼
HTML Tree
      │
      ├── Title
      ├── Body
      └── Image Tags
```

---

# 📌 Important Concepts

| Concept | Description |
|----------|-------------|
| Web Scraping | Extracting information from websites |
| requests | Downloads webpage content |
| BeautifulSoup | Parses HTML |
| HTML Parser | Converts HTML into searchable objects |
| GET Request | Retrieves webpage data |
| Status Code | Indicates request result |
| `response.content` | Raw HTML source |
| `find_all()` | Finds all matching HTML tags |
| `get_text()` | Extracts text without HTML tags |

---

# 📖 Code Examples

### Import libraries

```python
import requests
from bs4 import BeautifulSoup
```

---

### Send request

```python
response = requests.get(url)
```

---

### Status code

```python
print(response.status_code)
```

---

### Parse HTML

```python
soup = BeautifulSoup(content, "html.parser")
```

---

### Print title

```python
print(soup.title)
```

---

### Print title text

```python
print(soup.title.get_text())
```

---

### Print body

```python
print(soup.body)
```

---

### Find all image tags

```python
images = soup.find_all("img")
```

---

# ⚠️ Common Mistakes

### Forgetting to install libraries

```bash
pip install requests
pip install beautifulsoup4
```

---

### Wrong parser name

Wrong

```python
BeautifulSoup(content, "parser")
```

Correct

```python
BeautifulSoup(content, "html.parser")
```

---

### Forgetting parentheses

Wrong

```python
soup.title.get_text
```

Correct

```python
soup.title.get_text()
```

---

### Request failure

Always check:

```python
response.status_code
```

If it isn't **200**, the webpage may not have loaded successfully.

---

# 📝 Key Takeaways

- Web scraping automates data collection from websites.
- `requests` is used to send HTTP GET requests.
- `response.status_code` verifies whether the request succeeded.
- `response.content` contains the webpage's HTML.
- BeautifulSoup parses HTML into a searchable object.
- `get_text()` extracts only readable text from HTML tags.
- `find_all()` returns every matching HTML element.
- BeautifulSoup makes navigating and extracting webpage content much easier.

---

# 🚀 Skills Practiced

- Installing Python packages
- Using `requests`
- Sending HTTP requests
- Understanding HTTP status codes
- Parsing HTML
- Using BeautifulSoup
- Extracting webpage titles
- Extracting webpage body content
- Searching HTML elements
- Working with HTML tags

---

# 💡 Reflection

Today I learned the basics of web scraping using Python. I installed and used the `requests` library to retrieve webpage content and parsed the HTML using BeautifulSoup. I practiced checking HTTP status codes, extracting the page title and body, and locating HTML elements with `find_all()`. This exercise introduced the core workflow of web scraping and showed how Python can automatically collect information from websites for further analysis.
