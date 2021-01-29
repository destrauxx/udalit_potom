import sqlite3 as sq

conn = sq.connect('example.db')
c = conn.cursor()

c.execute("CREATE TABLE user (name text, email text)")
c.execute("INSERT INTO user VALUES ('Mike', 'mike@mike.com')")

conn.commit()
conn.close()