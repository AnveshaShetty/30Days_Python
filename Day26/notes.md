# Day 26 - Introduction to Flask, Templates & Static Files

# 🎯 Topics Covered

- Introduction to Flask
- Creating a Flask Application
- Flask Routing
- Running the Flask Server
- Dynamic Templates
- Jinja2 Template Engine
- Template Inheritance
- HTML Templates
- Forms
- GET & POST Requests
- Redirects
- Static Files (CSS)
- URL Generation
- Project Structure

---

# 📚 Introduction

**Flask** is a lightweight Python web framework used to build web applications.

Unlike Django, Flask provides only the essentials, allowing developers to add features as needed.

Flask is ideal for:

- Learning web development
- Building REST APIs
- Personal projects
- Small to medium web applications
- Prototypes

The project for this day uses a virtual environment with Flask installed before creating the web application.

---

# 1. Flask Project Structure

```
python_for_web/
│
├── app.py
├── templates/
│   ├── layout.html
│   ├── home.html
│   ├── about.html
│   └── post.html
│
├── static/
│   └── css/
│       └── main.css
│
└── venv/
```

---

# 2. Importing Flask

```python
from flask import Flask
```

Other useful imports include:

```python
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
```

The application imports these modules to handle routing, templates, forms, redirects, and URL generation.

---

# 3. Creating a Flask Application

```python
app = Flask(__name__)
```

`__name__` tells Flask where the application is located.

The project initializes the Flask app and configures static file caching. 

---

# 4. Flask Routing

A **route** connects a URL with a Python function.

Example

```python
@app.route('/')
def home():
    return "Hello World"
```

When the user visits

```
http://localhost:5000/
```

the `home()` function executes.

---

# 5. Home Route

Example

```python
@app.route('/')
def home():
    techs = ['HTML','CSS','JavaScript','Python','Flask']
    return render_template(...)
```

The home route passes a list of technologies, a page name, and a title to the template.

---

# 6. About Route

Example

```python
@app.route('/about')
def about():
```

Displays the About page.

This route renders the About template with a page title and application name. 

---

# 7. Result Route

Example

```python
@app.route('/result')
```

Used after processing the submitted form.

The project returns a separate result template for this route. 

---

# 8. POST Route

Example

```python
@app.route('/post',
           methods=['GET','POST'])
```

Allows both

- GET
- POST

requests.

The application shows the form on GET requests and processes submitted text on POST requests. 

---

# 9. GET Request

A GET request is used to retrieve information.

Example

```
Open webpage
```

No data is modified.

In the application, the GET request displays the Text Analyzer page. 

---

# 10. POST Request

POST sends data to the server.

Example

```python
content = request.form['content']
```

Used when a user submits a form.

The submitted text is retrieved from the form and printed before redirecting to the result page. 

---

# 11. Redirect

```python
redirect(url_for('result'))
```

Redirects the user to another route.

This project redirects to the `/result` page after a successful form submission.

---

# 12. Running the Server

```python
if __name__ == "__main__":
    app.run(debug=True)
```

`debug=True`

- Auto reload
- Shows detailed errors

The project runs the server on host `0.0.0.0` and uses port `5000` (or an environment-defined port).

---

# 13. HTML Templates

Instead of returning plain text,

Flask can return HTML.

Example

```python
return render_template("home.html")
```

Templates are stored inside the **templates** folder.

---

# 14. Jinja2 Template Engine

Flask uses **Jinja2**.

Variables

```html
{{ name }}
```

Loops

```html
{% for tech in techs %}
```

Condition

```html
{% if title %}
```

These template features are used throughout the HTML files.

---

# 15. Displaying Variables

Example

```html
<h1>{{name}}</h1>
```

Displays a Python variable inside HTML.

The Home and About templates display the application name dynamically.

---

# 16. Loops in Templates

Example

```html
{% for tech in techs %}
<li>{{tech}}</li>
{% endfor %}
```

Prints every technology passed from Python.

This loop is used to list technologies on the Home page. 

---

# 17. Template Inheritance

Instead of repeating HTML,

Flask uses

```html
{% extends "layout.html" %}
```

This makes

- reusable layouts
- cleaner code
- easier maintenance

The Home, About and Post templates all extend `layout.html`. 

---

# 18. Blocks

```html
{% block content %}
...
{% endblock %}
```

The child template inserts content into the parent layout.

The main layout defines the content block. 

---

# 19. Base Layout

A common layout contains

- Header
- Navigation
- CSS links
- Main content

Every page inherits from this layout.

The shared layout also includes navigation links generated with `url_for()`.

---

# 20. Navigation Menu

Example

```html
<a href="/">Home</a>

<a href="/about">About</a>
```

Provides navigation between pages.

The project uses `url_for()` for generating navigation URLs. 

---

# 21. Forms

HTML Form

```html
<form method="POST">
```

Collects user input.

The Text Analyzer page contains a form with a textarea and submit button.

---

# 22. Textarea

```html
<textarea></textarea>
```

Allows multiple lines of text.

Used for text analysis input.

---

# 23. Submit Button

```html
<input
type="submit">
```

Sends form data to Flask.

The page labels the button **Process Text**. 

---

# 24. Static Files

Static files include

- CSS
- Images
- JavaScript

Flask stores them inside

```
static/
```

---

# 25. CSS in Flask

Example

```html
<link
href="{{ url_for('static',
filename='css/main.css') }}">
```

Flask generates the correct path for the stylesheet. 

---

# 26. Styling

The CSS file styles

- Background
- Navigation bar
- Fonts
- Headings
- Paragraphs

The stylesheet defines colors, spacing, typography and layout for the application. 

---

# 📊 Request Flow

```
Browser
   │
   ▼
Flask Route
   │
   ▼
Python Function
   │
   ▼
Render Template
   │
   ▼
HTML + CSS
   │
   ▼
Browser Output
```

---

# 📌 Flask Functions

| Function | Purpose |
|----------|----------|
| Flask() | Create application |
| render_template() | Render HTML |
| request | Read request data |
| redirect() | Redirect user |
| url_for() | Generate URLs |
| app.run() | Start server |

---

# 📌 Jinja Syntax

| Syntax | Purpose |
|---------|----------|
| `{{ variable }}` | Display variable |
| `{% for %}` | Loop |
| `{% if %}` | Condition |
| `{% extends %}` | Template inheritance |
| `{% block %}` | Content section |

---

# 📌 HTTP Methods

| Method | Purpose |
|----------|----------|
| GET | Retrieve page |
| POST | Submit data |

---

# 📌 Project Files

| File | Purpose |
|------|----------|
| app.py | Flask application |
| layout.html | Base template |
| home.html | Home page |
| about.html | About page |
| post.html | Text Analyzer form |
| main.css | Styling |

---

# ⚠️ Common Mistakes

### Forgetting render_template()

❌

```python
return "home.html"
```

✅

```python
return render_template("home.html")
```

---

### Forgetting methods=['POST']

❌

```python
@app.route('/post')
```

✅

```python
@app.route('/post',
methods=['GET','POST'])
```

---

### Using Static File Incorrectly

❌

```html
<link href="main.css">
```

✅

```html
<link
href="{{ url_for('static',
filename='css/main.css') }}">
```

---

### Forgetting Template Inheritance

Instead of duplicating HTML,

Use

```html
{% extends "layout.html" %}
```

---

# 🚀 Skills Practiced

- Creating Flask applications
- Flask routing
- Rendering HTML templates
- Passing variables to templates
- Jinja2 syntax
- Loops in templates
- Template inheritance
- Handling GET requests
- Handling POST requests
- Reading form data
- Redirecting users
- Using CSS in Flask
- Building a multi-page web application

---

# 📝 Key Takeaways

- Flask is a lightweight Python web framework.
- Routes connect URLs with Python functions.
- `render_template()` renders HTML pages.
- Jinja2 allows variables, loops, and conditions inside HTML.
- `layout.html` provides a reusable base template.
- Forms send data to Flask using GET or POST methods.
- Static resources such as CSS are stored in the `static` folder.
- `url_for()` generates URLs for routes and static files automatically.

---

# 💡 Reflection

Today I built my first multi-page Flask web application. I learned how to define routes, render HTML templates, use Jinja2 for dynamic content, handle GET and POST requests, create forms, organize templates with inheritance, and apply CSS through Flask's static folder. These concepts form the foundation of Python web development.
