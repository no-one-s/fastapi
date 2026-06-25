# Summary of "Using Templates in FastAPI" Video Transcript

## [00:00 ~ 01:03] Introduction to Templates in FastAPI

This section introduces the topic of using templates in FastAPI. The presenter outlines the scope of the tutorial, highlighting that templates allow serving HTML pages alongside the existing JSON API endpoints. Key learning objectives include:

- setting up Jinja2 templates
- passing data to templates
- using Jinja2 syntax for loops and conditionals
- implementing template inheritance with a `layout.html`
- adding Bootstrap for styling
- configuring static files such as CSS and images

The goal is to create a visually appealing blog homepage displaying posts with a styled layout.

## [00:32 ~ 02:40] Why Use Templates?

The instructor explains why HTML templates are crucial in web applications. Returning raw HTML strings in Python is manageable only for very simple uses, but for full pages with complex structure—headers, navigation bars, footers, and styling—it becomes unwieldy.

Templates enable defining proper HTML files and injecting dynamic data cleanly. While API routes should return JSON for programmatic consumption, human users prefer styled HTML pages. Templates allow both audiences to be served by the same backend data.

## [01:40 ~ 03:42] Starting Point and Current Application State

The presenter reviews the current state of the codebase, referencing the existing `main.py` from a previous tutorial. The application is running with a simple home route returning raw HTML and an `/api/posts` route returning JSON.

The presenter restarts the app using `uvicorn` and demonstrates the browser output: a basic `h1` tag with a post title on the homepage, and JSON output at the API route containing dummy posts.

## [03:42 ~ 05:36] Setting Up Jinja2 Templates

Jinja2 is introduced as FastAPI’s templating engine, which FastAPI installs automatically if using the recommended standard installation. If not pre-installed, a manual installation is required:

```bash
pip install Jinja2
```

The tutorial updates imports to include:

```python
from fastapi import Request
from fastapi.templating import Jinja2Templates
```

The outdated `HTMLResponse` import is removed. A new `templates` directory is created to hold HTML template files. FastAPI is configured with:

```python
templates = Jinja2Templates(directory="templates")
```

## [05:36 ~ 08:40] Creating and Using the First Template - home.html

A basic `home.html` file is created inside the `templates` folder, containing simple HTML with a title, header, and paragraph.

The home route is modified to return a template response instead of raw HTML. The route function now accepts a `request` parameter and returns:

```python
return templates.TemplateResponse("home.html", {"request": request})
```

Refreshing the browser renders the static HTML template.

## [08:40 ~ 11:54] Passing Data to Templates and Using Jinja2 Syntax

The presenter passes a variable named `posts` containing an array of post data to the template context.

In the template, Jinja2 syntax is used for loops and printing variables:

```html
{% for post in posts %}
  <h2>{{ post.title }}</h2>
  <p>{{ post.content }}</p>
{% endfor %}
```

Jinja2 allows accessing dictionary keys with dot notation, e.g. `post.title`, making the template cleaner.

## [11:54 ~ 14:28] Using Conditional Statements in Templates

Conditional rendering is shown using `{% if %}`:

```html
{% if title %}
  <title>FastAPI blog - {{ title }}</title>
{% else %}
  <title>FastAPI blog</title>
{% endif %}
```

The route passes `title="home"` so the browser tab shows a customized title.

## [14:28 ~ 18:46] Template Inheritance with layout.html for Code Reuse

Template inheritance is introduced to reduce duplication. A base template named `layout.html` contains shared structure like `<head>`, navigation, and footer.

A named block is defined:

```html
{% block content %}{% endblock %}
```

Child templates like `home.html` extend it:

```html
{% extends "layout.html" %}
{% block content %}
<!-- page-specific content here -->
{% endblock %}
```

This allows consistent global elements with page-specific content.

## [18:46 ~ 23:26] Adding Styling with Bootstrap and Custom CSS

The instructor upgrades `layout.html` to a fuller version named `layout_finished.html` with:

- Open Graph meta tags
- Google Fonts
- Bootstrap CDN links
- custom stylesheet `main.css` under `/static/css`
- a Bootstrap navigation bar
- a content block for child templates
- a sidebar placeholder
- footer with copyright
- Bootstrap JS imports
- a dark mode toggle

The completed `home_finished.html` retains the same extension and loops over posts, showing metadata like author and post date.

A hard refresh reveals styling fails until static files are served.

## [23:26 ~ 28:44] Configuring Static Files for CSS, JavaScript, and Images

Static files are introduced as non-dynamic resources served as-is. The project structure includes subfolders for:

- CSS (`main.css`)
- JavaScript (`utils.js`)
- icons
- profile pictures
- `site.webmanifest`

The directory is mounted as `static`:

```python
from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static")
```

After this setup, assets such as `/static/css/main.css` are accessible and the page loads styles correctly.

## [28:44 ~ 32:43] Using `url_for` in Templates for Route and Static File Links

Templates are improved by using `url_for` instead of hardcoded paths.

Example route link:

```html
<a href="{{ url_for('home') }}">Home</a>
```

Example static asset link:

```html
<link href="{{ url_for('static', path='css/main.css') }}" rel="stylesheet">
```

This makes URLs maintainable if backend paths change.

## Explicit Route Naming

When routes have multiple decorators, `url_for` can become ambiguous. The fix is to name routes explicitly:

```python
@app.get("/", include_in_schema=False, name="home")
@app.get("/post", include_in_schema=False, name="post")
def home():
    ...
```

This ensures `url_for("home")` points to `/` and `url_for("post")` points to `/post`.

## [32:43 ~ 37:34] Recap and Next Steps

The presenter reviews the major concepts:

- creating the templates directory and configuring FastAPI templates
- passing dynamic data to templates via context dictionaries
- using Jinja2 syntax for loops and conditionals
- implementing template inheritance for reusable layout code
- adding Bootstrap and custom CSS for styling
- setting up static files and mounting the static directory
- using `url_for` for route and asset URLs
- separating JSON API endpoints from HTML-rendered pages

The video closes with a preview of the next tutorial, covering URL parameters and individual post pages with validation and error handling.

## Viewer Notes

Viewers are invited to leave questions in the comments, support the tutorials by liking and sharing, and subscribe for future videos.

## Key Technical Concepts and Code Snippets

### Setting up templates

```python
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
```

### Returning a template response

```python
@app.get("/", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "posts": posts})
```

### Jinja2 syntax examples in HTML

```html
{% for post in posts %}
  <h2>{{ post.title }}</h2>
  <p>{{ post.content }}</p>
{% endfor %}

{% if title %}
  <title>FastAPI blog - {{ title }}</title>
{% else %}
  <title>FastAPI blog</title>
{% endif %}
```

### Template inheritance

```html
<!-- layout.html -->
<body>
  {% block content %}{% endblock %}
</body>

<!-- home.html -->
{% extends "layout.html" %}
{% block content %}
<!-- page-specific content here -->
{% endblock %}
```

### Serving static files

```python
from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static")
```

### Using `url_for` in templates

```html
<link href="{{ url_for('static', path='css/main.css') }}" rel="stylesheet">
<a href="{{ url_for('home') }}">Home</a>
```

### Explicit route naming for `url_for`

```python
@app.get("/", include_in_schema=False, name="home")
@app.get("/post", include_in_schema=False, name="post")
def home():
    ...
```

This video provides a robust foundation for building FastAPI web applications with clean, maintainable HTML templating, styling, static file handling, and URL management using modern FastAPI and Jinja2 best practices.
