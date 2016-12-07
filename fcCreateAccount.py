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

    def createUser(self, name, uid, pw): #users have a first name, username, and password
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
        #used substituted parameters to avoid injection flaws
        #selects a user and password that matches the parameters
        #sending both a plaintext username and password through a server is a big no-no!
        #planning to implement hashing authentication :)
        c.execute('SELECT password FROM USEREntries WHERE username = ? AND password = ?', (uid,pw))
        return c.fetchone() != None #returns True if the user exists
