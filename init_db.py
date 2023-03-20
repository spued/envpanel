import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('00:00-05:00', 'Environment display system')
            )
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('06:00-08:00', 'Environment display system')
            )
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('09:00-12:00', 'Environment display system')
            )
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('13:00-15:00', 'Environment display system')
            )
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('16:00-18:00', 'Environment display system')
            )
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('18:00-22:00', 'Environment display system')
            )
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('22:00-23:00', 'Environment display system')
            )

#cur.execute("INSERT INTO setting_data (brightness, systemname) VALUES (?, ?)",('50,50,50,50,50', 'ENVDISPLAY'))

connection.commit()
connection.close()
