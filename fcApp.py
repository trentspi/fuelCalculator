from bottle import static_file, run, template, route, post, request, error
from fuelCalculator import * #import FC class

@route('/static/<filepath:path>') #static route for files in the static folder
def server_static(filepath):
    return static_file(filepath, root='./static/') #returns static files (W3.CSS)

@route('/') #main route, displays index.html
def index():
  return template('index.html')

@post('/')
def calMPG(): #data requested upon form submission (calculate button)
    distbefore = int(request.forms.get('distbefore'))
    distafter = int(request.forms.get('distafter'))
    date = request.forms.get('date')
    price = float(request.forms.get('price'))
    gallons = float(request.forms.get('gallons'))

    f = fuelCalculator()
    f.date = date
    f.pricegas = price
    f.gallonsgas = gallons
    f.setMilesRange(distbefore, distafter)
    f.pricepg(price, gallons)
    rv = [
        {"id": 0, "date": "{}".format(f.date)},
        {"id": 1, "mpg": "{}".format(f.mpg())},
        {"id": 2, "miles": "{}".format(f.miles)},
        {"id": 3, "gallons": "{}".format(f.gallonsgas)},
        {"id": 4, "priceg": "{}".format(f.pricegas)},
        {"id": 5, "pricepg": "{}".format(f.pricepg)}
        ]
    return dict(data=rv)

run(host= "localhost", port = 8081, debug = True, reloader = True)
