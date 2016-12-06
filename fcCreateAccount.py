import sqlite3, json
class fcCreateAccount(object):
    def startDB(self):
        conn = sqlite3.connect('fcData.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE USEREntries (
            name text,
            username text,
            password text)'''
            )
        conn.commit()
        conn.close()

    def createUser(self, name, uid, pw):
        conn = sqlite3.connect('fcData.db')
        c = conn.cursor()
        c.execute('''INSERT INTO USEREntries (
            name,
            username,
            password
            )
            VALUES (?,?,?)''',
            (
                name,
                uid,
                pw
            )
        )
        conn.commit()
        conn.close()

    def checkUser(self, uid, pw):
        conn = sqlite3.connect('fcData.db')
        c = conn.cursor()
        c.execute('SELECT password FROM USEREntries WHERE username = ? AND password = ?', (uid,pw))
        return c.fetchone() != None
