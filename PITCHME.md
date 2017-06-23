---

# Bottle.py

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
