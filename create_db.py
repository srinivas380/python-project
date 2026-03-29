import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
''')

c.execute('''
CREATE TABLE places (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    image TEXT
)
''')

c.execute("INSERT INTO places (name, description, image) VALUES ('Goa', 'Beach place', 'goa.jpg')")
c.execute("INSERT INTO places (name, description, image) VALUES ('Delhi', 'Capital city', 'delhi.jpg')")

conn.commit()
conn.close()