from bottle import static_file, run, template, route, get, post, request, error, redirect
from fuelCalculator import *
from fcStartDB import *
from fcCreateAccount import *
import json, sqlite3, os.path

@error(404) #Error in routing handling
def error404(error):
    return template('error.html')

@route('/static/<filepath:path>') #static route for files in the static folder
def server_static(filepath):
    return static_file(filepath, root='./static/') #returns static files (W3.CSS, main.CSS)

@route('/signup')
def loadSignup():
    return template('signup.html')

@route('/') #main route, displays index.html
def loadLogin():
    return template('login.html')

@route('/calculate')
def loadIndex():
    return template('index.html')

@route('/getMPG', method = "POST")
def loadData():
    s = fcStartDB()
    uid = request.forms.get("userid")
    uid = request.forms.get("userid")
    print("username from loadData {}".format(uid))
    return s.loadDB(uid)


@post('/signup')
def signup():
    databasePresent = os.path.isfile('./fcData.db') #check for created database file
    s = fcCreateAccount()
    f = fcStartDB()
    if databasePresent == False:
        s.startDB()
        f.startDB()
    fname = request.forms.get('fname')
    username = request.forms.get('username')
    password = request.forms.get('password')
    s.createUser(fname, username, password)
    redirect('/')

@post('/')
def login():
    s = fcCreateAccount()
    rv = ""
    uname = request.forms.get('username')
    pword = request.forms.get('password')

    if s.checkUser(uname, pword):

        rv = {
        "username": uname,
        "password": pword
        }

    return json.dumps(rv)

@post('/calculate')
def calcMPG():
    try:
        username = request.forms.get('userid')
        print("username found in bottle route: {}".format(username))
        distbefore = request.forms.get('distbefore')
        distafter = request.forms.get('distafter')
        date = request.forms.get('date')
        print(request.forms.get('price'))
        price = float(request.forms.get('price'))
        gallons = float(request.forms.get('gallons'))

    except ValueError:
        print("ERROR, NO VALUE ENTERED FOR CALCULATION")

    print("date: {}".format(date))
    f = fuelCalculator()
    f.date = date
    print("f.date: {}".format(f.date))
    f.pricegas = price
    f.gallonsgas = gallons
    f.setMilesRange(distbefore, distafter)
    f.pricepg(price, gallons)

    conn = sqlite3.connect('fcData.db')
    c = conn.cursor()
    c.execute('''INSERT INTO MPGEntries (
                    username,
                    date,
                    mpg,
                    miles,
                    gallonsgas,
                    pricegas,
                    pricepg
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)''',
                (
                    username,
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
        "userid": username,
        "date": f.date,
        "mpg": f.mpg(),
        "miles": f.miles,
        "gallonsgas": f.gallonsgas,
        "pricegas": "$" + str(f.pricegas),
        "pricepg": "$" + str(f.pricepgi)
    }

    return json.dumps(rv)

run(host= "localhost", port = 8080, debug = True, reloader = True)
