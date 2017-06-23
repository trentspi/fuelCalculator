---

# Bottle.py

---

Bottle is a fast, simple and lightweight WSGI micro web-framework for Python. It is distributed as a single file module and has no dependencies other than the Python Standard Library.

---

# Routing 

Requests to function-call mapping with support for clean and dynamic URLs.

---

# Templates

Fast and pythonic built-in template engine and support for mako, jinja2 and cheetah templates.

---

# Utilities

Convenient access to form data, file uploads, cookies, headers and other HTTP-related metadata.

---

# Server

Built-in HTTP development server and support for paste, fapws3, bjoern, gae, cherrypy or any other WSGI capable HTTP server.

---

Hello World with Bottle.py

```
from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)
```

---

Fuel Calculator with Bottle

http://github.com/trentspi/fuelCalculator

---

Technologies Used

- Bottle.py
- SQLite3
- JQuery
- W3.CSS

---

Trenton Spice - Computer Science @ IUPUI

Web developer @ Cole's Marketing
Python research project (SCATE) @ SEDS IUPUI

http://github.com/trentspi

http://linkedin.com/in/trentonspice
