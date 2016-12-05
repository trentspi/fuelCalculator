from bottle import static_file, run, template, route, get, post, request, error
from fuelCalculator import * #import FC class
from fcStartDB import * #import FC start database class
import json, sqlite3, os.path

@error(404)
def error404(error):
    return template('error.html')

@route('/static/<filepath:path>') #static route for files in the static folder
def server_static(filepath):
    return static_file(filepath, root='./static/') #returns static files (W3.CSS, main.CSS)

@route('/') #main route, displays index.html

def index():
    return template('index.html')

@post('/')
def calMPG():
    databasePresent = os.path.isfile('./fcData.db')
    if databasePresent == False:
        s = fcStartDB()
        s.startDB()

    try:
        distbefore = int(request.forms.get('distbefore'))
        distafter = int(request.forms.get('distafter'))
        date = request.forms.get('date')
        price = float(request.forms.get('price'))
        gallons = float(request.forms.get('gallons'))
    except ValueError:
        print("ERROR, NO VALUE ENTERED FOR CALCULATION")

    f = fuelCalculator()
    f.date = date
    f.pricegas = price
    f.gallonsgas = gallons
    f.setMilesRange(distbefore, distafter)
    f.pricepg(price, gallons)

    conn = sqlite3.connect('fcData.db')
    c = conn.cursor()
    c.execute('''INSERT INTO MPGEntries (
                    date,
                    mpg,
                    miles,
                    gallonsgas,
                    pricegas,
                    pricepg
                )
                VALUES (?, ?, ?, ?, ?, ?)''',
                (
                    f.date,
                    f.mpg(),
                    f.miles,
                    f.gallonsgas,
                    f.pricegas,
                    f.pricepgi,
                )
            )
    conn.commit()
    conn.close()

    rv = {
        "date": f.date,
        "mpg": f.mpg(),
        "miles": f.miles,
        "gallonsgas": f.gallonsgas,
        "pricegas": "$" + str(f.pricegas),
        "pricepg": "$" + str(f.pricepgi)
    }

    return json.dumps(rv)


run(host= "localhost", port = 8080, debug = True, reloader = True)
