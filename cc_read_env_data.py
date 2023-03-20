import sqlite3

def get_db_connection():
    conn = sqlite3.connect('/home/sunya/envpanel/database.db')
    conn.row_factory = sqlite3.Row
    return conn

conn = get_db_connection()
rows = conn.execute('SELECT * FROM env_data ORDER BY id DESC LIMIT 30').fetchall()
for row in rows:
    print(row[0],row[1])
conn.close()
