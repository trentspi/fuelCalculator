import sqlite3, json
class fcStartDB(object):
    def startDB(self):
        conn = sqlite3.connect('fcData.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE MPGEntries (
                    id integer primary key,
                    username text,
                    date text,
                    mpg real,
                    miles integer,
                    gallonsgas real,
                    pricegas real,
                    pricepg real)'''
                )
        conn.commit()
        conn.close()

    def loadDB(self, uid):
        conn = sqlite3.connect('fcData.db')
        c = conn.cursor()
        c.execute('SELECT * FROM MPGEntries WHERE username = ?', (uid,))
        data = c.fetchall()
        conn.close()
        print(json.dumps(data))
        return json.dumps(data)
