from bottle import static_file, run, template, route, post, request, error
from fuelCalculator import * #import FC class
import json

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

    rv = {
        "date": f.date,
        "mpg": f.mpg(),
        "miles": f.miles,
        "gallonsgas": f.gallonsgas,
        "pricegas": "$" + str(f.pricegas),
        "pricepg": "$" + str(f.pricepgi)
    }
    print(f.pricepg)
    return json.dumps(rv)

run(host= "localhost", port = 8080, debug = True, reloader = True)
