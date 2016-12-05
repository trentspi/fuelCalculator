import sqlite3
class fcStartDB(object):
    def startDB(self):
        conn = sqlite3.connect('fcData.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE MPGEntries (
                    id integer primary key,
                    userid text,
                    date text,
                    mpg real,
                    miles integer,
                    gallonsgas real,
                    pricegas real,
                    pricepg real)'''
                )
        conn.commit()

        conn.close()
